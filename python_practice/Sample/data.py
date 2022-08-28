## This file is stil throwing error....need to debug how to connect to localhost...should an instance of server should run in parallel or SQL server instance should run?---Need to explore..

import mysql.connector as SQLC
# Establishing connection with the SQL
 
DataBase = SQLC.connect(
  host ="localhost",
  user ="user name",
  password ="password"
)
# Cursor to the database
Cursor = DataBase.cursor()
 
Cursor.execute("CREATE DATABASE margam-data")
print("Margam Farms database is created")

