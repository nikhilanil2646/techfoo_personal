import sqlite3

conn = sqlite3.connect('users.db')

"""conn.execute('''CREATE TABLE USERS
         (EMPID INT PRIMARY KEY     NOT NULL,
         NAME           TEXT    NOT NULL,
         EMAIL            INT     NOT NULL,
         PASSWORD        CHAR(50));'''
data = conn.execute("delete from USERS")"""


conn.execute(" CREATE TABLE Role (Id INTEGER primary key AUTOINCREMENT, Name varchar(30))")
conn.commit()

conn.execute("insert into Role(Name) values('Admin');")
conn.commit()
conn.execute("insert into Role(Name) values('Staff');")
conn.commit()




conn.execute("CREATE TABLE Users (Id INTEGER primary key AUTOINCREMENT,FirstName varchar(30),LastName varchar(30),Email varchar(30),Password varchar(20),Contact int);")
conn.commit()

conn.execute("insert into Users(FirstName,LastName,Email,Password,Contact) values ('shivangi','joshi','shivangi.joshi@intimetec.com','1234',988334444);")
conn.commit()

conn.execute("insert into Users(FirstName,LastName,Email,Password,Contact) values ('Nikhil','Bansal','nikhil.bansal@intimetec.com','1234',7988816585);")
conn.commit()

conn.execute("insert into Users(FirstName,LastName,Email,Password,Contact) values ('harshita','agarwal','harshita.agarwal@intimetec.com','1234',988334444);")
conn.commit()

conn.execute("insert into Users(FirstName,LastName,Email,Password,Contact) values ('lakshya','dosi','lakshya.dosi@intimetec.com','1234',986834444);")
conn.commit()

conn.execute("insert into Users(FirstName,LastName,Email,Password,Contact) values ('rohit','agarwal','rohit.agarwal@intimetec.com','1234',988339944);")
conn.commit()

conn.execute("insert into Users(FirstName,LastName,Email,Password,Contact) values ('anuj','sharma','anuj.sharma@intimetec.com','1234',9883343454);")
conn.commit()
            


conn.execute("CREATE TABLE Food (Id int identity(1,1) primary key,Name varchar(30),Description varchar(100),UnitPrice int,IsActive bit,CreatedDate date,ModifiedDate date,CreatedBy int,FOREIGN KEY (CreatedBy) REFERENCES Users(Id),ModifiedBY int,FOREIGN KEY (ModifiedBY) REFERENCES Users(Id)")
conn.commit()
	


def get_users(cmd):
    data_object = conn.execute(cmd)
    data = data_object.fetchall()
    for item in data:
        col_names = [tup[0] for tup in data_object.description]
        row_values = [i for i in item]
        row_as_dict = dict(zip(col_names,row_values))
        print(row_as_dict)

get_users("Select * from Users")
get_users("Select * from Role")