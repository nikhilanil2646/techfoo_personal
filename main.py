from flask import Flask, request
from flask_cors import CORS, cross_origin
from flask_restful import Resource, Api
from json import dumps
from flask_jsonpify import jsonify
from python_src.users_db import *

app = Flask(__name__)
api = Api(app)

CORS(app)

@app.route("/")
def hello():
    return jsonify({'text':'Hello World!'})

@app.route('/api/users', methods = ['POST'])
def new_user():
    email = request.json.get('email')
    password = request.json.get('password')
    print("Input credentials:",email, password)
    user=get_user(email, password)

    if user==False:
        return jsonify({'text':'Failed'})
    return jsonify(user)


if __name__ == '__main__':
   app.run(port=5002)