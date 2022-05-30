from flask import Flask, request
from flask_cors import CORS, cross_origin
from flask_restful import Resource, Api
from json import dumps
from flask_jsonpify import jsonify
from python_src.users_db import *
from python_src.food_db import *
from python_src.orders_db import *

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

@app.route('/api/getallfood', methods = ['GET'])
def get_all_food():
    all_food=get_all_food_from_db()
    if all_food==False:
        return jsonify({'text':'No data found ....'})
    return jsonify(all_food)

@app.route('/api/getfoodbyid/<food_id>', methods = ['GET'])
def get_food_by_id(food_id):
    food=get_food_by_id_from_db(food_id)
    if food==False:
        return jsonify({'text':'No data found ....'})
    return jsonify(food)

@app.route('/api/getorderhistorybyuserid/<user_id>', methods = ['GET'])
def get_all_orders_by_userid(user_id):
    orderhistory=get_all_orders_by_userid_from_db(user_id)
    if orderhistory==False:
        return jsonify({'text':'No data found ....'})
    print("Returning. ....",orderhistory )
    return jsonify(orderhistory)

@app.route('/api/getorderdetailsbyorderrid/<order_id>', methods = ['GET'])
def get_order_details_by_orderid(order_id):
    orderdetails=get_order_details_by_orderid_from_db(order_id)
    if orderdetails==False:
        return jsonify({'text':'No data found ....'})
    print("Returning. ....",orderdetails )
    return jsonify(orderdetails)


if __name__ == '__main__':
   app.run(port=5002)