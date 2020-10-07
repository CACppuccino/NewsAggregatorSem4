from flask import Flask, request, jsonify, url_for, render_template, send_from_directory
from flask_cors import CORS, cross_origin
from minitask.simple_search import simple_match_search
from elasticsearch import Elasticsearch
from summary_1.summary import body_summary

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

@app.route('/search')
@cross_origin()
def search():
    query = request.args.get('query', None)
    if query:
        print('query is %s' % query)
        res = simple_match_search(ES, INDEX_NAME, query)
        list_res = res['hits']['hits']
        for one in list_res:
            sum=body_summary((one['_source'])['art'])
            (one['_source'])['art'] = sum[0]+sum[1]
        return jsonify(list_res)
    return jsonify([])

if __name__ == '__main__':
    app.run(debug=True)