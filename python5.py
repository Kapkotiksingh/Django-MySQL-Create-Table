import mysql.connector as mysql

db = mysql.connect(
    host = 'localhost',
    user = 'root',
    password = 'kamal@123#',
    database = "datacamp"
)

cursor = db.cursor()

## creating a table called 'users' in the 'datacamp' database
cursor.execute("CREATE TABLE users (name VARCHAR(255), user_name VARCHAR(255))")