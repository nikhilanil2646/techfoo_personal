import sqlite3


conn = sqlite3.connect('users.db')

data=conn.execute("select f.Id,f.Name as FoodName,f.UnitPrice,f.IsActive,f.CreatedDate,f.ModifiedDate,f.CreatedBy,f.ModifiedBY,f.CategoryId,f.ImageURL,c.Name as CategoryName from Food as f inner join Category as c on c.Id=f.CategoryId")

for item in data:
    print(item)