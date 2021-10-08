from input_parser import Parser
import dir_search
import flask
from flask import request, jsonify

base = ""

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def home():
    return ""

@app.route('/search', methods=['GET'])
def search_basic():
    if 'q' in request.args:
        name = request.args['q']
    else:
        return "Error: No search query provided. Please provide one."
    p = Parser(dir_search.basic(name))
    p.parse()
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

app.run()
