# install MySQL on your PC
# pip install mysql
# pip install mysql-connector
# pip install mysql-connector-python

import mysql.connector

database = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = ''
)

cursor = database.cursor()

cursor.execute("CREATE DATABASE crmapp1")
print("All done")