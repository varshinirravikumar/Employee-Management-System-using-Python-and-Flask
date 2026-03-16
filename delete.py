import mysql.connector
con= mysql.connector.connect(host="localhost",user="root",password="",database="pythonproject")

id = input("Enter the Employee Id you want to delete:")

cur = con.cursor()
query = "delete  from emp_details where id = %s"
cur.execute(query,(id,))
con.commit()
print("\n")
print("Deleted Successfully")