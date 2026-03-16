import mysql.connector
con = mysql.connector.connect(host="localhost",user="root",password="",database="pythonproject")

cursor = con.cursor()
id = input("Enter the Employee Id:")
query = "select * from emp_details where id = %s"
cursor.execute(query,(id,))
result = cursor.fetchone()

if result:
    print("\n Current Details:")
    print("Id:",result[0])
    print("Name:",result[1])
    print("Age:",result[2])
    print("DoB:",result[3])
    print("Department:",result[4])
    print("Designation:",result[5])
    print("Address:",result[6])
    print("Phone:",result[7])
    print("Salary:",result[8])

    print("\nPress Enter if you don't want to change the value")

    id = input("New Id")
    name = input("New Name:")
    age = input("New Age:")
    dob = input("New DoB:")
    department = input("New Department:")
    designation = input("New Designation:")
    address = input("New Address:")
    phone = input("New Phone no:")
    salary = input("New Salary:")

    if id == "":
        id = result[0]
    if name == "":
        name = result[1]
    if age == "":
        age = result[2]
    if dob == "":
        dob = result[3]
    if department == "":
        department = result[4]
    if designation == "":
        designation = result[5]
    if address == "":
        address = result[6]
    if phone == "":
        phone = result[7]
    if salary == "":
        salary = result[8]
    
    
    cursor.execute("update emp_details set id = %s,name = %s,age = %s,dob = %s,department = %s,designation =%s,address = %s,phone = %s,salary = %s" ,(id,name,age,dob,department,designation,address,phone,salary))
    con.commit()
    print("\nRecord Updated Successfully")

else:
    print("Employee not found")

con.close()

