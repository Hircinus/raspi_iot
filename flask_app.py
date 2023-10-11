
# A very simple Flask Hello World app for you to get started with...

from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello from Flask!'


my_dataset = [{'id':0,'name':'The Title' }, {'id':1,'name':' Title2'}]
@app.route('/api/v1/resources/movies', methods=['GET'])
def api_all():
    return jsonify(my_dataset)
