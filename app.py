from flask import Flask, request, jsonify, url_for, render_template, send_from_directory
from flask_cors import CORS, cross_origin
from minitask.simple_search import simple_match_search
from elasticsearch import Elasticsearch
from knn_indexing.index import knn_query


INDEX_NAME = 'news'
ES = Elasticsearch([{'host' : 'localhost', 'port': 9200}])
app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/')
def index_page():
    return render_template('index.html')

@app.route('/css/<path:filename>')
def send_css(filename):
    return send_from_directory('static/css', filename)

@app.route('/js/<path:filename>')
def send_js(filename):
    return send_from_directory('static/js', filename)

@app.route('/origin_search')
@cross_origin()
def search():
    query = request.args.get('query', None)
    if query:
        print('query is %s' % query)
        res = simple_match_search(ES, INDEX_NAME, query)
        list_res = res['hits']['hits']
        return jsonify(list_res)
    return jsonify([])

@app.route('/search')
@cross_origin()
def knn_search():
    query = request.args.get('query', None)
    if query:
        res = knn_query(query)
        list_res = res['hits']['hits']
        return jsonify(list_res)
    return jsonify([])

if __name__ == '__main__':
    app.run(debug=True)
