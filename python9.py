import mysql.connector as mysql


db = mysql.connect(
    host = 'localhost', 
    user = 'root',
    password = 'kamal@123#',
    database = 'datacamp'
)

cursor = db.cursor()


## dropping the 'id' column
cursor.execute("ALTER TABLE users DROP id")

cursor.execute("DESC users")

print(cursor.fetchall())