import sqlite3

def execute_command(command):
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

def get_role(user_data):
    pass
def check_credentials(user_data):
    command=f"Select * from Users where Email='{user_data['email']}'"
    db_data=execute_command(command)
    if not db_data or db_data["Email"]!=user_data['email'] or db_data["Password"]!=user_data["password"]:
        return False
    return db_data

def get_user(email, password):
    user_data= {"email":email, "password":password}
    try:
        user=check_credentials(user_data)
        del user["Password"]
    except:
        return False
    if not user:
        return False
    return user