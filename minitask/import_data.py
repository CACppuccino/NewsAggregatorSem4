import pandas as pd
import requests
import json

from elasticsearch import Elasticsearch as es

from elasticsearch import helpers as h

"""
Need to create the index first before using this script
curl -XPUT https://localhost:9200/example3 --insecure -u admin:admin

After index is created, run this script to import data in tf-idf format
python import_data.py
"""
URL = 'https://localhost:9200/example3/_doc/'

# the code with idea inspired by https://www.cnblogs.com/shaosks/p/7592229.html

def start_import(test_size = 1000):

    data_set  = json.loads(open ('./result.json').read())
    total_number = len(data_set)
    print('in total: ', total_number)

    data_set_test = data_set[:test_size]

    elastic_search = start_elastic_search()

    # df = pd.read_csv('./extractor.csv')

    # print(df.iloc[0])

    # for index, row in df.iterrows():

    #     data=dict(title=row['article_title'], url=row['article_url'], content=row['article_content'])
    #     print('adding: ', data['title'])
    #     index_elastic_search(data, elastic_search, index)

    if not elastic_search.indices.exists( index = 'news'):
        # create the index
	    elastic_search.indices.create(index = 'news')

    for x in range(test_size):
        print('adding: ', data_set_test[x]['title'])
        index_elastic_search(data_set_test[x], elastic_search, x)
        # print('inserting:', data['title'])
        # res = requests.post(URL+str(index), json=data, auth=('admin', 'admin'), verify=False)
        # print('get response: ', res.text)
        # if res.json().get('status', 200) >= 400:
        #     print('*'*90)

    search_index_test(elastic_search)

def index_elastic_search(data, elastic_search, index):
    '''parameter: data, dictionary with title, url, content'''
    # print(data)
    
    try:

        # index_result = elastic_search.index(index='news', doc_type='web_news', body=data)

        index_result = elastic_search.index(index='news', body=data, id=index)
    except:
        print(data)
    print('success')

def start_elastic_search():

    ip_url = ["127.0.0.1"]

    # initialize elastic search

    new_es = es(ip_url, timeout=35, max_retries=8, retry_on_timeout=True)
    return new_es

def search_index_test(elastic_search):

    # test with query to match 'ACT'

    q = "president"

    position = "title"

    test1 = {
            "query": {
                "match": {
                    position: q
                }
            }
        }

    # output = elastic_search.search(index='news', doc_type='web_news', body=test1)

    print('\n', 'searching for keyword: ', q, " ", "in", " article ", position, '\n')

    output = elastic_search.search(index='news', body=test1)

    print('searching finished with total time: ', output['took'], '\n')

    print('result: ', '\n')

    for hit in output['hits']['hits']:

        # print search result
        
        print ('match news title: ', hit['_source']['title'], '\n', 'match news link: ', hit['_source']['link'], '\n', '-------------------------------------------------------------')

if __name__ == '__main__':
    start_import()
