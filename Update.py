import mysql.connector
con= mysql.connector.connect(host="localhost",user="root",password="",database="pythonproject")
def update():
    print("1.Name")
    print("2.Age")
    print("3.DoB")
    print("4.Department")
    print("5.Designation")
    print("6.Address")
    print("7.Phone")
    print("8.Salary")

    option = int(input("Enter the number Field which you want to update"))
    if option == 1:
        id = input("Enter Employee id:")
        name = input("Enter the name to be updated:")
        cur = con.cursor()
        query = "update emp_details set name=%s where id = %s"
        cur.execute(query,(name,id))
        con.commit()
        print("\n")
        print("Name Updated Successfully")

    elif option ==2:
        id = input("Enter Employee id:")
        age = input("Enter the Age to be updated:")
        cur = con.cursor()
        query = "update emp_details set age = %s where id = %s"
        cur.execute(query,(age,id))
        con.commit()
        print("\n")
        print("Age Updated Successfully")

    elif option == 3:
        id = input("Enter Employee id:")
        dob = input("Enter the Date of Birth to be updated:")
        cur = con.cursor()
        query = "update emp_details set  dob=%s where id = %s"
        cur.execute(query,(dob,id))
        con.commit()
        print("\n")
        print("DoB Updated Successfully")
    elif option == 4:
        id = input("Enter Employee id:")
        department = input("Enter the Department to be updated:")
        cur = con.cursor()
        query = "update emp_details set department = %s where id = %s"
        cur.execute(query,(department,id))
        con.commit()
        print("\n")
        print("Department Updated Successfully")
    elif option == 5:
        id = input("Enter Employee id:")
        designation = input("Enter the Designation to be updated:")
        cur = con.cursor()
        query = "update emp_details set designation = %s where id = %s"
        cur.execute(query,(designation,id))
        con.commit()
        print("\n")
        print("Designation Updated Successfully")
    elif option == 6:
        id = input("Enter Employee id:")
        address = input("Enter the address to be updated:")
        cur = con.cursor()
        query = "update emp_details set address = %s where id = %s"
        cur.execute(query,(address,id))
        con.commit()
        print("\n")
        print("Address Updated Successfully")
    elif option == 7:
        id = input("Enter Employee id:")
        phone = input("Enter the phone number to be updated:")
        cur = con.cursor()
        query = "update emp_details set phone = %s where id = %s"
        cur.execute(query,(phone,id))
        con.commit()
        print("\n")
        print("Phone number Updated Successfully")
    elif option == 8:
        id = input("Enter Employee id:")
        salary = input("Enter the salary to be updated:")
        cur = con.cursor()
        query = "update emp_details set salary = %s where id = %s"
        cur.execute(query,(salary,id))
        con.commit()
        print("\n")
        print("Salary Updated Successfully")
    else:
        print("Invalid Field")



while True:
    print("\n")
    print("1.Update Record")
    choice=int(input("Enter the choice:")) 
    if choice == 1:
        update()
    else:
        print("Invalid choice")