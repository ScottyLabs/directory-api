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
def search():
    if 'q' in request.args:
        name = request.args['q']
    else:
        return "Error: No name field provided. Please specify a name."
    p = Parser(dir_search.basic(name))
    p.parseSingle()
    return jsonify(p.results)

app.run()
