from flask import Flask, request, jsonify
from minitask.simple_search import simple_match_search
from elasticsearch import Elasticsearch


INDEX_NAME = 'news'
ES = Elasticsearch([{'host' : 'localhost', 'port': 9200}])
app = Flask(__name__)


@app.route('/search')
def search():
    query = request.args.get('query', None)
    if query:
        print('query is %s' % query)
        res = simple_match_search(ES, INDEX_NAME, query)
        list_res = res['hits']['hits']
        return jsonify(list_res)
    return jsonify([])

if __name__ == '__main__':
    app.run(debug=True)
