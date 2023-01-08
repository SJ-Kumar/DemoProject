import mysql.connector
db_connection = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="root"
)
print(db_connection)