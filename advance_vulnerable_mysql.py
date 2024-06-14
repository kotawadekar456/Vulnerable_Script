import mysql.connector 
from datetime import date,datetime

exp_level = 1

print("Please select Level of exploit\n")
print("1. Low")
print("2. Advance")

exp_level = int(input())

if exp_level == 1:

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

	    query = "select 1 from user where username='"+username+"' and password='"+password+"'"
	    
	    print(query)
	    f.write(query+"\n")
	    
	    cursor.execute(query)

	    result = cursor.fetchall()

	    for i in result:
	    	log_cursor = log_cursor + 1

	    if log_cursor >=1:
	    	print("Authentication Successful")
	    	f.write("Authentication Successful")
	    else: 
	    	print("Authentication Failed")
	    	f.write("Authentication Failed")
	    f.close()
	    cursor.close()

	    conn_obj.close()

if exp_level == 2:
	username = input("Enter Username")
	password = input("Enter Password")
	
	if username.find("'")> -1 or password.find("'")> -1:
		print(username)
		print(password)
		print("SQL injection detected")
	else:
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

		    query = "select 1 from user where username='"+username+"' and password='"+password+"'"
		    
		    print(query)
		    f.write(query+"\n")
		    
		    cursor.execute(query)

		    result = cursor.fetchall()

		    for i in result:
		    	log_cursor = log_cursor + 1

		    if log_cursor >=1:
		    	print("Authentication Successful")
		    	f.write("Authentication Successful")
		    else: 
		    	print("Authentication Failed")
		    	f.write("Authentication Failed")
		    f.close()
		    cursor.close()

		    conn_obj.close()
