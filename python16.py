import mysql.connector as mysql


db = mysql.connect(
    host = 'localhost',
    user = 'root',
    password = 'kamal@123#',
    database = 'datacamp'
)

cursor = db.cursor()

## defining the Query
query = "SELECT * FROM users WHERE id = 5"

## getting records from the table
cursor.execute(query)

## fetching all records from the 'cursor' object
records = cursor.fetchall()

## Showing the data
for record in records:
    print(record)