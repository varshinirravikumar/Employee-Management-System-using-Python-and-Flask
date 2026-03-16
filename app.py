from flask import Flask,render_template,request,redirect
import mysql.connector

app = Flask(__name__)
con= mysql.connector.connect(host="localhost",user="root",password="",database="pythonproject")

@app.route("/")
def login_page():
    return render_template("login.html")

@app.route("/login",methods=["POST"])
def login():
    username = request.form['username']
    password = request.form['password']
    con = mysql.connector.connect(host="localhost",user="root",password="",database="pythonproject")
    cur = con.cursor()
    query = "Select * from logintable where username= %s and password = %s"
    cur.execute(query,(username,password))
    result =cur.fetchone()
    if result:
        return redirect("/main")
    else:
        return("Invalid Username and Password")
@app.route("/signout")
def sign():
    return render_template("login.html")
# Show employee table
@app.route("/main")
def main():
    return render_template("main.html")
@app.route("/select")
def employees():
    cur = con.cursor()
    cur.execute("SELECT * FROM emp_details")
    data = cur.fetchall()
    return render_template("select.html", employees=data)


# Show insert form
@app.route("/add")
def add():
    return render_template("insert.html",msg=None)


# Insert employee
@app.route("/insert", methods=['POST'])
def insert():

    name = request.form['name']
    age = request.form['age']
    dob = request.form['dob']
    designation = request.form['designation']
    department = request.form['department']
    address = request.form['address']
    phone = request.form['phone']
    salary = request.form['salary']

    cursor = con.cursor()
    query = """INSERT INTO emp_details(name,age,dob,designation,department,address,phone,salary)VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"""
    cursor.execute(query,(name,age,dob,designation,department,address,phone,salary))
    con.commit()
    return render_template("insert.html",msg="Employee Inserted Successfully")
# Delete employee
@app.route("/employees")
def delete_page():
    cur = con.cursor()
    cur.execute("SELECT * FROM emp_details")
    data = cur.fetchall()
    return render_template("delete.html", employees=data)
@app.route("/delete/<int:id>")
def delete(id):
    cur = con.cursor()
    cur.execute("DELETE FROM emp_details WHERE id=%s",(id,))
    con.commit()
    return redirect("/employees")

# Show update page
@app.route("/update")
def update_page():
    return render_template("update.html")


@app.route("/update_employee", methods=["POST"])
def update_employee():
    id = request.form['id']
    name = request.form['name']
    age = request.form['age']
    dob = request.form['dob']
    designation = request.form['designation']
    department = request.form['department']
    address = request.form['address']
    phone = request.form['phone']
    salary = request.form['salary']

    cur = con.cursor()
    query = """UPDATE emp_details SET name=%s, age=%s, dob=%s, designation=%s,department=%s, address=%s, phone=%s, salary=%s WHERE id=%s"""
    cur.execute(query,(name,age,dob,designation,department,address,phone,salary,id))
    con.commit()
    return render_template("update.html",msg="Updated Successfully")


@app.route("/fetch_employee", methods=["POST"])
def fetch_employee():
    id = request.form['id']

    cur = con.cursor()
    cur.execute("SELECT * FROM emp_details WHERE id=%s", (id,))
    data = cur.fetchone()
    return render_template("update.html", emp=data)


if __name__ == '__main__':
    app.run(debug=True)