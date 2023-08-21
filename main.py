import mysql.connector

conn = mysql.connector.connect(host="localhost",port="3306",user="admin",password="welcome",database="mark_management_system")
cursor = conn.cursor()
selectQuery = "select * from students"
cursor.execute(selectQuery)
records = cursor.fetchall()

for i in range(5):
    print(f"Id:{records[i][0]}")
    print(f"Name:{records[i][1]}")
    print(f"Dob:{records[i][2]}")
    print(f"Roll No:{records[i][3]}\n")


cursor.close()
conn.close()