import sqlite3
import os

os.remove("./users.db")

conn = sqlite3.connect('users.db')


conn.execute(" CREATE TABLE Role (Id INTEGER primary key AUTOINCREMENT, Name varchar(30))")
conn.execute("CREATE TABLE Users (Id INTEGER primary key AUTOINCREMENT,FirstName varchar(30),LastName varchar(30),Email varchar(30),Password varchar(20),Contact int);")
conn.execute("CREATE TABLE UserRole (Id INTEGER primary key AUTOINCREMENT,UserId INTEGER, RoleId INTEGER, FOREIGN KEY(UserId) REFERENCES Users (Id), FOREIGN KEY(RoleId) REFERENCES Role (Id));")
conn.execute("CREATE TABLE Food (Id INTEGER primary key AUTOINCREMENT,Name varchar(30),Description varchar(100),UnitPrice INTEGER,IsActive bit,CreatedDate date,ModifiedDate date,CreatedBy INTEGER,ModifiedBY INTEGER,CategoryId INTEGER, ImageURL VARCHAR(50), FOREIGN KEY (CreatedBy) REFERENCES Users(Id),FOREIGN KEY (ModifiedBY) REFERENCES Users(Id),FOREIGN KEY (CategoryId) REFERENCES Category(Id))")
conn.execute("CREATE TABLE Category(Id INTEGER primary key AUTOINCREMENT,Name nvarchar(100),IsActive bit)")
conn.execute("CREATE TABLE Orders(Id INTEGER primary key AUTOINCREMENT,OrderDateTime datetime,TotalAmt INTEGER,Status INTEGER,UserId int,FOREIGN KEY (Status) REFERENCES OrderStatus (Id),FOREIGN KEY (UserId) REFERENCES Users (Id));")
conn.execute("CREATE TABLE OrderDetails(Id INTEGER primary key AUTOINCREMENT,Quantity INTEGER,Price INTEGER,OrderId INTEGER,FoodId INTEGER,FOREIGN KEY (OrderId) REFERENCES Orders (Id),FOREIGN KEY (FoodId) REFERENCES Food (Id));")
conn.execute("CREATE TABLE OrderStatus(Id INTEGER primary key AUTOINCREMENT,Status varchar(20));")


conn.executescript('''
insert into Role(Name) values('Admin');
insert into Role(Name) values('Staff');
''')
conn.commit()

conn.executescript('''
insert into Users(FirstName,LastName,Email,Password,Contact) values ('shivangi','joshi','shivangi.joshi@intimetec.com','1234',988334444);
insert into Users(FirstName,LastName,Email,Password,Contact) values ('Nikhil','Bansal','nikhil.bansal@intimetec.com','1234',7988816585);
insert into Users(FirstName,LastName,Email,Password,Contact) values ('harshita','agarwal','harshita.agarwal@intimetec.com','1234',988334444);
insert into Users(FirstName,LastName,Email,Password,Contact) values ('lakshya','dosi','lakshya.dosi@intimetec.com','1234',986834444);
insert into Users(FirstName,LastName,Email,Password,Contact) values ('rohit','agarwal','rohit.agarwal@intimetec.com','1234',988339944);
insert into Users(FirstName,LastName,Email,Password,Contact) values ('anuj','sharma','anuj.sharma@intimetec.com','1234',9883343454);
''')
conn.commit()
            
conn.executescript('''
    insert into UserRole(UserId,RoleId) values (1,2);
    insert into UserRole(UserId,RoleId) values (2,2);
    insert into UserRole(UserId,RoleId) values (3,2);
    insert into UserRole(UserId,RoleId) values (4,2);
''')
conn.commit()

conn.executescript('''
    insert into Food(Name,Description,UnitPrice,IsActive,CreatedDate,ModifiedDate,CreatedBy,ModifiedBY,CategoryId,ImageURL) values('Burger','spicy burger with cheese',100,1,'2021-07-01','2021-08-01',1,1,2,"shorturl.at/ghjC4");
    insert into Food(Name,Description,UnitPrice,IsActive,CreatedDate,ModifiedDate,CreatedBy,ModifiedBY,CategoryId,ImageURL) values('Dosa','Dosa with chutney',140,1,'2021-07-01','2021-08-01',1,1,3,"shorturl.at/nrAT8");
    insert into Food(Name,Description,UnitPrice,IsActive,CreatedDate,ModifiedDate,CreatedBy,ModifiedBY,CategoryId,ImageURL) values('Sandwich','Grilled Sandwich with extra cheese',70,1,'2021-07-01','2021-08-01',1,1,2,"shorturl.at/iyOTV");
    insert into Food(Name,Description,UnitPrice,IsActive,CreatedDate,ModifiedDate,CreatedBy,ModifiedBY,CategoryId,ImageURL) values('Mango Shake','Mango Shake with Vanilla Ice-Cream',80,1,'2021-07-01','2021-08-01',1,1,4,"shorturl.at/myGV8");
''')
conn.commit()


conn.executescript('''
    insert into Category(Name,IsActive) values("Lunch",1);
    insert into Category(Name,IsActive) values("BreakFast",1);
    insert into Category(Name,IsActive) values("FastFood",1);
    insert into Category(Name,IsActive) values("Dinner",1);    
''')
conn.commit()


conn.executescript("insert into Orders(OrderDateTime,TotalAmt,Status,UserId) values('2021-07-01',1000,1,1);")
conn.executescript("insert into Orders(OrderDateTime,TotalAmt,Status,UserId) values('2021-07-01',500,1,3);")
conn.executescript("insert into Orders(OrderDateTime,TotalAmt,Status,UserId) values('2021-07-24',160,1,5);")
conn.executescript("insert into Orders(OrderDateTime,TotalAmt,Status,UserId) values('2021-07-01',300,0,4);")
conn.executescript("insert into Orders(OrderDateTime,TotalAmt,Status,UserId) values('2021-07-04',1500,1,4);")
conn.executescript("insert into Orders(OrderDateTime,TotalAmt,Status,UserId) values('2021-07-04',1500,2,4);")
conn.executescript("insert into Orders(OrderDateTime,TotalAmt,Status,UserId) values('2021-07-11',1000,1,2);")
conn.commit()


conn.executescript('''
    insert into OrderDetails(Quantity,Price,OrderId,FoodId) values(10,1000,1,1);
    insert into OrderDetails(Quantity,Price,OrderId,FoodId) values(10,1000,1,3);
    insert into OrderDetails(Quantity,Price,OrderId,FoodId) values(10,1000,1,2);
    insert into OrderDetails(Quantity,Price,OrderId,FoodId) values(10,1000,3,1);
    insert into OrderDetails(Quantity,Price,OrderId,FoodId) values(10,1000,2,3);
    insert into OrderDetails(Quantity,Price,OrderId,FoodId) values(10,1000,2,1);
    insert into OrderDetails(Quantity,Price,OrderId,FoodId) values(10,1000,2,4);
''')



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
get_users("Select * from UserRole")
get_users("select * from Food")
get_users("select f.Id,f.Name as FoodName,f.UnitPrice,f.IsActive,f.CreatedDate,f.ModifiedDate,f.CreatedBy,f.ModifiedBY,f.CategoryId,f.ImageURL,c.Name as CategoryName from Food as f inner join Category as c on c.Id=f.CategoryId")
get_users("select f.Id,f.Name as FoodName,f.UnitPrice,f.IsActive,f.CreatedDate,f.ModifiedDate,f.CreatedBy,f.ModifiedBY,f.CategoryId,c.Name as CategoryName from Food as f inner join Category as c on c.Id=f.CategoryId where f.Id=4")
get_users("select o.Id as OrderId,o.OrderDateTime,o.TotalAmt,o.status as StatusId,os.Status,o.UserId from orders o left join orderStatus os on os.id=o.status where o.UserId=4")
get_users("Select OD.Id as OrderDetailId, OD.Quantity as qty, OD.Price, OD.OrderId, OD.FoodId, F.UnitPrice as AmountPerUnit,F.Name,F.Description From OrderDetails OD left join Food F on F.id=OD.FoodId Where OrderID=1")
get_users("Select OD.Id as OrderDetailId, OD.Quantity as qty, OD.Price, OD.OrderId, OD.FoodId, F.UnitPrice as AmountPerUnit,F.Name,F.Description From OrderDetails OD left join Food F on F.id=OD.FoodId")