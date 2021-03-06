import sqlite3

from python_src.food_db import insert_data

def fetch_all_data(command):
    conn = sqlite3.connect('users.db')
    data_object = conn.execute(command)
    data = data_object.fetchall()
    dict_data={}
    try:
        dict_data=[]
        for item in data:
            col_names = [tup[0] for tup in data_object.description]
            row_values = [i for i in item]
            dict_row = dict(zip(col_names,row_values))
            dict_data.append(dict_row)
        return dict_data
    except:
        print("Error in fetching data from db....")


def insert_data(cmd):
        conn = sqlite3.connect('users.db')
        print(cmd)
        conn.execute(cmd)
        conn.commit()
        return True


def fetch_one_data(command):
    conn = sqlite3.connect('users.db')
    data_object = conn.execute(command)
    data = data_object.fetchall()
    dict_data={}
    try:
        for item in data:
            col_names = [tup[0] for tup in data_object.description]
            row_values = [i for i in item]
            dict_row = dict(zip(col_names,row_values))
            return dict_row
    except:
        print("Error in fetching data from db....")


def get_all_orders_by_userid_from_db(user_id):
    command = f"select o.Id as OrderId,o.OrderDateTime,o.TotalAmt,o.status as StatusId,os.Status,o.UserId from orders o left join orderStatus os on os.id=o.status where o.UserId={user_id}"
    db_orders=fetch_all_data(command)
    return db_orders

def get_order_details_by_orderid_from_db(order_id):
    command = f"Select OD.Id as OrderDetailId, OD.Quantity as qty, OD.Price, OD.OrderId, OD.FoodId, F.UnitPrice as AmountPerUnit,F.Name,F.Description From OrderDetails OD left join Food F on F.id=OD.FoodId Where OrderID={order_id}"
    db_orders=fetch_all_data(command)
    return db_orders

def get_all_order_from_db():
    cmd = ("Select OD.Id as OrderDetailId, OD.Quantity as qty, OD.Price, OD.OrderId, OD.FoodId, F.UnitPrice as AmountPerUnit,F.Name,F.Description From OrderDetails OD left join Food F on F.id=OD.FoodId")
    db_orders=fetch_all_data(cmd)
    return db_orders

def update_order_status_in_db(status, orderid):
    cmd = (f"Update orders set status={status} where Id={orderid}")
    db_orders=insert_data(cmd)
    return db_orders

def create_order_in_db(order_details):
    cmd = f'''insert into Orders(OrderDateTime,TotalAmt,Status,UserId) values('{order_details["OrderDateTime"]}',{order_details["TotalAmt"]},{order_details["Status"]},{order_details["UserId"]});'''
    conn = sqlite3.connect('users.db')
    cursor=conn.cursor()
    cursor.execute(cmd)
    conn.commit()
    cursor = cursor.execute('SELECT max(Id) FROM Orders')
    order_id = cursor.fetchone()[0]
    #order_id = conn.lastrowid
    print("-------------->>>>>>>>>>Order id",order_id)
    for order in order_details["orderDetails"]:
        cmd = f'''insert into OrderDetails(Quantity,Price,OrderId,FoodId) values({order["Quantity"]},{order["Price"]},{order_id},{order["FoodId"]});'''
        cursor.execute(cmd)
        conn.commit()
    return True


