from elasticsearch import Elasticsearch
import tensorflow as tf
import tensorflow_hub as hub
import numpy as np

"""
Create an index for knn
curl -XPUT --header "Content-Type: application/json" "https://localhost:9200/knn_index3" -d '{"settings": 
                                                        {
                                                         "index.knn": true
                                                        }, 
                                                     "mappings": 
                                                        {"properties":
                                                            {"feature1": 
                                                                {"type": "knn_vector",
                                                                 "dimension": 2
                                                                 }
                                                            }
                                                        }
                                                    }' -u admin:admin --insecure
"""

# Use 50 dimension vectors to fasten the process
module_url = "https://tfhub.dev/google/nnlm-en-dim50/2"

# Create an instance of a client, not verifying the SSL certificate and not giving warning because of that
es = Elasticsearch("https://admin:admin@localhost:9200", verify_certs=False, ssl_show_warn=False)

# Create knn_index if not already exist
if not es.indices.exists("knn_index"):
    es.indices.create("knn_index", {"settings": {"index.knn": True},
                                    "mappings": {"properties": {"title_v": {"type": "knn_vector", "dimension": 50},
                                                                "title": {"type": "text"}}}})
    print("Created knn index")

# Used for vectorisation
embed = hub.KerasLayer(module_url)


# Turn a sentence into vectors
def vectorise_sent(sent: str):
    words = sent.split(" ")
    vs = np.zeros((1*50))
    for word in words:
        x = tf.constant([word])
        embeddings = embed(x)
        x = np.asarray(embeddings)
        vs = vs + x
    vs = (vs / len(words)).tolist()  # Faster, and more likely to have "king-man+woman = queen" relationship
    return vs[0]


# Extract titles from index example3
example3_titles = es.search(index="example3", filter_path=["hits.hits._source.title"])
titles = []
for news in example3_titles["hits"]["hits"]:
    title = news["_source"]["title"]
    titles.append(title)

vectors = []
for title in titles:
    vectors.append(vectorise_sent(title))
print("titles extracted")

# Insert title data into knn_index
for i in range(len(titles)):
    title = titles[i]
    title_v = vectors[i]
    es.create(index="knn_index", id=i, body={"title_v": title_v, "title": title})
print("titles indexed")

# Test searching with vector
query = "corona virus"
query_v = vectorise_sent(query)
search_body = {
    "query": {
        "knn": {
            "title_v": {
                "vector": query_v,
                "k": 4
            }
        }
    }
}
results = es.search(index="knn_index", body=search_body, filter_path=["hits.hits._source.title"])
for result in results["hits"]["hits"]:
    print(result)
