import pymysql

db = pymysql.connect("localhost", "root", "46281234", "mis")

cursor = db.cursor()

cursor.execute("SELECT VERSION()")

data = cursor.fetchone()

print("Database version : %s " % data)
