import mysql.connector 
from datetime import date,datetime

username = input("Enter Username")
password = input("Enter Password")

log_cursor = 0
f = open("log.txt","a")
f.write("\n----------------\n")
access_log = "User "+username+" tries to login to application on "+str(datetime.now())
f.write(access_log)
print(access_log)

        
conn_obj = mysql.connector.connect( host='localhost', database='swapnil', user='swapnil',password='abc@123')

if conn_obj.is_connected():
    f.write("\nConnected to database\n")

    cursor = conn_obj.cursor()

    query = "select * from user where username='"+username+"' and password='"+password+"'"
    
    f.write(query+"\n")
    
    cursor.execute(query)

    result = cursor.fetchall()

    for i in result:
        log_cursor = log_cursor +1

    if log_cursor >=1:
        print("Authentication Successful")
        f.write("Authentication Successful")
    else: 
        print("Authentication Failed")
        f.write("Authentication Failed")
    f.close()
    cursor.close()

    conn_obj.close()

