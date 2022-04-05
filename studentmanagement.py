from flask import Flask, render_template, request
import sqlite3 as sql

connection = sql.connect("studentflask.db", check_same_thread=False)
listOfStudTable = connection.execute("select name from sqlite_master where type='table' AND name='students'").fetchall()

if listOfStudTable != []:
    print("Table is already Created.")
else:
    connection.execute('''create table students(
                            ID integer primary key autoincrement,
                            name text,
                            branch text,
                            admno integer,
                            rolno integer,
                            dob text,
                            sem integer,
                            password text                             
                            )''')
    print("Table Created Successfully")

student = Flask(__name__)


@student.route("/")
def Login_details():
    return render_template("studentLogin.html")


@student.route("/register", methods=["GET", "POST"])
def Register():
    if request.method == 'POST':
        getName = request.form["name"]
        getBranch = request.form["branch"]
        getAdmno = request.form["admno"]
        getRolno = request.form["rolno"]
        getDob = request.form["dob"]
        getSem = request.form["sem"]
        getPass = request.form["pass"]
        getConPass = request.form["cpass"]
        print(getName)
        print(getBranch)
        print(getAdmno)
        print(getRolno)
        print(getDob)
        print(getSem)
        print(getPass)
        print(getConPass)
        try:
            connection.execute("insert into students(name,branch,admno,rolno,dob,sem,password)\
                           values('" + getName + "','" + getBranch + "'," + getAdmno + "," + getRolno + ",'" + getDob + "'," + getSem + ",'" + getPass + "')")
            connection.commit()
            print("Student Data Added Successfully.")
        except:
            print("Error occured")
    return render_template("register.html")


@student.route("/search")
def Search():
    return render_template("search.html")


@student.route("/delete")
def Delete():
    return render_template("delete.html")


if __name__ == "__main__":
    student.run()

