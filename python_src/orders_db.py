import sqlite3

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

