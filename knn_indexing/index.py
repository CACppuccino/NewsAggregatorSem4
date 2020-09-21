import re
from elasticsearch import Elasticsearch
import json
from knn_indexing import __settings__ as s
import tensorflow as tf
import tensorflow_hub as hub
import numpy as np
import re
import datetime


es = Elasticsearch(s.URL, verify_certs=False, ssl_show_warn=False)
index_name = "knn_index"
if not es.indices.exists(index_name):
    es.indices.create(index_name, {"settings": {"index.knn": True},
                                   "mappings": {"properties": {"title_v": {"type": "knn_vector", "dimension": 50},
                                                               "title": {"type": "text"},
                                                               "art_v": {"type": "knn_vector", "dimension": 50},
                                                               "article": {"type": "text"}}}})
    print("Created knn index")
else:
    print("Index already exists")

# Used for vectorisation
embed = hub.load(s.MODEL_URL)
print("Model loaded")


# Turn a sentence into vectors
def vectorise_sent(sent: str):
    sent = re.sub(r"[^\w\s]", "", sent)
    words = sent.split(" ")
    vs = np.zeros((1*50))
    for word in words:
        x = tf.constant([word])
        embeddings = embed(x)
        x = np.asarray(embeddings)
        vs = vs + x
    vs = (vs / len(words)).tolist()  # Faster, and more likely to have "king-man+woman = queen" relationship
    return vs[0]


data_list = json.loads(open("../minitask/result.json").read())
print("Data loaded")

for i in range(len(data_list)):
    data = data_list[i]
    title = data["title"]
    title_v = vectorise_sent(data["title"])
    article = data["art"]
    art_v = vectorise_sent(data["art"])
    es.create(index=index_name, body={"title_v": title_v, "title": title, "art_v": art_v, "article": article}, id=i)
    print(i, "inserted:", title)

print("Insert Completed")


"""
Only support searching of one field. Either title_v or art_v. Could create a functionality of choosing search field
"""
print("Test searching")
query = "airforce"
title_v = vectorise_sent(query)
search_body = {
    "query": {
        "knn": {
            "art_v": {
                "vector": title_v,
                "k": 10
            }
        }
    }
}
start = datetime.datetime.now()
results = es.search(index=index_name, body=search_body, filter_path=["hits.hits._source.title"])
duration = datetime.datetime.now() - start
print("Duration:", duration)
for result in results["hits"]["hits"]:
    print(result)
