import mysql.connector
con = mysql.connector.connect(host="localhost",user="root",password="",database="logindb")
username = input("Enter your Username:")
password = input("Enter Password:")

cur = con.cursor()
query = "Select * from logintable where username= %s and password = %s"
cur.execute(query,(username,password))
result =cur.fetchone()
if result:
    print("Login Successfull")
else:
    print("Invalid Username and Password")