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

def get_all_food_from_db():
    print("Starting.")
    command=f"select f.Id,f.Name as FoodName,f.UnitPrice,f.IsActive,f.CreatedDate,f.ModifiedDate,f.CreatedBy,f.ModifiedBY,f.CategoryId,f.ImageURL,c.Name as CategoryName from Food as f inner join Category as c on c.Id=f.CategoryId"
    db_food=fetch_all_data(command)
    print("Script completed", db_food)
    return db_food


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


def get_food_by_id_from_db(food_id):
    command = f"select f.Id,f.Name as FoodName,f.UnitPrice,f.IsActive,f.CreatedDate,f.ModifiedDate,f.CreatedBy,f.ModifiedBY,f.CategoryId,f.ImageURL,c.Name as CategoryName from Food as f inner join Category as c on c.Id=f.CategoryId where f.Id={food_id}"
    db_food=fetch_one_data(command)
    return db_food

