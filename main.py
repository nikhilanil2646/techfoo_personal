from urllib import response
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

@app.route('/api/insertfood', methods = ['POST'])
def insert_food():
    food = {}
    food['Name'] = request.json.get('Name')
    food['Description'] = request.json.get("Description")
    food['UnitPrice'] = request.json.get("UnitPrice")
    food['IsActive'] = request.json.get("IsActive")
    food['CreatedDate'] = request.json.get("CreatedDate")
    food['ModifiedDate'] = request.json.get("ModifiedDate")
    food['CreatedBy'] = request.json.get("CreatedBy")
    food['ModifiedBY'] = request.json.get("ModifiedBY")
    food['CategoryId'] = request.json.get("CategoryId")
    food['ImageURL'] = request.json.get("ImageURL")
    response = insert_food_in_db(food)
    
    if response==False:
        return jsonify({'text':'Failed'})
    return jsonify({'text':'Data inserted'})

@app.route('/api/getallorders', methods = ['GET'])
def get_all_orders():
    allorders=get_all_order_from_db()
    if allorders==False:
        return jsonify({'text':'No data found ....'})
    print("Returning. ....",allorders )
    return jsonify(allorders)

@app.route('/api/updateorderstatus', methods = ['POST'])
def update_order_status():
    status = request.json.get("status")
    orderid = request.json.get("orderid")
    response = update_order_status_in_db(status, orderid)
    if response==False:
        return jsonify({'text':'Failed'})
    return jsonify({'text':'Status Updated'})

@app.route('/api/placeorder', methods = ['POST'])
def place_order():
    orderdetail = {}
    orderdetail["OrderDateTime"] = request.json.get("OrderDateTime")
    orderdetail["TotalAmt"] = request.json.get("TotalAmt")
    orderdetail["Status"] = request.json.get("Status")
    orderdetail["UserId"] = request.json.get("UserId")
    orderdetail["orderDetails"] = request.json.get("orderDetails")
    response = create_order_in_db(orderdetail)
    if response==False:
        return jsonify({'text':'Failed'})
    return jsonify({'text':'Order placed...'})


if __name__ == '__main__':
   app.run(port=5002)