import mysql.connector
from tabulate import tabulate
con= mysql.connector.connect(host="localhost",user="root",password="",database="pythonproject")

cur = con.cursor()
query = "select * from emp_details"
cur.execute(query)
result =cur.fetchall()
print("\n")
print(tabulate(result,headers=["Id","Name","Age","DoB","Department","Designation","Address","Phone no","Salary"]))