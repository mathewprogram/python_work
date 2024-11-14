import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Passw0rd!",
    database="test0001"
)

cursor = conn.cursor()
cursor.execute("SELECT * FROM Cliente")
for row in cursor.fetchall():
    print(row)

conn.close()
