import re
from input_parser import Parser
import dir_search
import flask
from flask import request, jsonify
from flask_cors import CORS

base = ""

app = flask.Flask(__name__)
app.config["DEBUG"] = True

CORS(app)


@app.route('/', methods=['GET'])
def home():
    return ""

@app.route('/search/basic/<search>', methods=['GET'])
def get_basic(search):
    p = Parser(dir_search.basic(search))
    p.parse()
    return jsonify(p.results)

@app.route('/search/basic', methods=['GET', 'POST'])
def post_basic():
    if request.method == 'GET':
        if 'query' in request.args:
            search = request.args['query']
            p = Parser(dir_search.basic(search))
            p.parse()
            return jsonify(p.results)
        return "Error: No search query provided. Please provide one."
    elif request.method == 'POST':
        search = request.form['search']
        p = Parser(dir_search.basic(search))
        p.parse()
        print(p.results)
        return jsonify(p.results)

@app.route('/search/advanced', methods=['GET'])
def search_advanced():
    first = None
    last = None
    id = None
    email = None
    if 'first' in request.args:
        first = request.args['first']
    if 'last' in request.args:
        last = request.args['last']
    if 'id' in request.args:
        id = request.args['id']
    if 'email' in request.args:
        email = request.args['email']
    if not any([first,last,id,email]):
        return "Error: No search query provided. Please provide one."
    p = Parser(dir_search.advanced(first, last, id, email))
    p.parse()
    return jsonify(p.results)

@app.route('/search/advanced', methods=['POST'])
def post_advanced():
    first = None
    last = None
    id = None
    email = None
    if 'first' in request.form:
        first = request.form['first']
    if 'last' in request.form:
        last = request.form['last']
    if 'id' in request.form:
        id = request.form['id']
    if 'email' in request.form:
        email = request.form['email']
    if not any([first,last,id,email]):
        return "Error: No search query provided. Please provide one."
    p = Parser(dir_search.advanced(first, last, id, email))
    p.parse()
    return jsonify(p.results)

app.run()
