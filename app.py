from flask import Flask, request, jsonify, url_for, render_template, send_from_directory
from flask_cors import CORS, cross_origin
from minitask.simple_search import simple_match_search
from elasticsearch import Elasticsearch
from summary_1.summary import body_summary
from knn_indexing.index import knn_query



# INDEX_NAME = 'news'

# ES = Elasticsearch([{'host' : 'localhost', 'port': 9200}])

INDEX_NAME = 'knn_index'

ES = Elasticsearch("https://admin:admin@localhost:9200", verify_certs=False, ssl_show_warn=False)

app = Flask(__name__)

cors = CORS(app) 
# the CORS header is for dev phase, when serving frontend and backend in different ports

app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/')
def index_page():
    """
    Index page returning the html file
    """
    return render_template('index.html')

@app.route('/css/<path:filename>')
def send_css(filename):
    """
    Routing the css static files
    """
    return send_from_directory('static/css', filename)

@app.route('/js/<path:filename>')
def send_js(filename):
    """
    Routing the js static files
    """
    return send_from_directory('static/js', filename)

@app.route('/origin_search')
@cross_origin()
def search():
    """
    Origin Search: use tf-idf index to search
    """
    query = request.args.get('query', None)
    if query:
        print('query is %s' % query)
        res = simple_match_search(ES, 'news', query)
        list_res = res['hits']['hits']
        for one in list_res:
            sum_txt = body_summary(one['_source']['art'])
            one['_source']['summary'] = ' '.join(sum_txt)
        return jsonify(list_res)
    return jsonify([])

@app.route('/search')
@cross_origin()
def knn_search():
    """
    KNN search: use K-ANN indexing to search, KNN plugin is needed here
    """
    query = request.args.get('query', None)
    if query:
        res = knn_query(query)
        list_res = res['hits']['hits']
        return jsonify(list_res)
    return jsonify([])

if __name__ == '__main__':
    app.run(debug=True)
