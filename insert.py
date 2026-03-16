import mysql.connector
con= mysql.connector.connect(host="localhost",user="root",password="",database="pythonproject")

name= input("Enter Employee name:")
age = input("Enter Age:")
dob = input("Enter Employee Date of Birth:")
designation = input("Enter Employee Designation:")
department = input("Enter Department:")
address = input("Enter Employee Address:")
phone = input("Enter Phone number:")
salary = input("Enter Employee Salary:")



cursor = con.cursor()
query = "insert into emp_details (name,age,dob,designation,department,address,phone,salary) values (%s,%s,%s,%s,%s,%s,%s,%s)"
cursor.execute(query,(name,age,dob,designation,department,address,phone,salary))
con.commit()
print("employee added")
