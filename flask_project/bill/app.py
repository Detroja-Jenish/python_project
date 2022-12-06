# write variable in upper case if that is used in templates
# use variable in uppercase in templates
from flask import Flask, render_template, redirect, request
import json
import math
from os import mkdir

app = Flask("__name__")

all_bill = []
this_bill = []
users = {} 

@app.route("/")
def index():
    return render_template("index.html")
@app.route("/signup-form")
def signup_form():
    return render_template("signup.html")

@app.route("/login-form")
def login_form():
    return render_template("login.html")

@app.route("/login", methods=["POST"])
def login():
    with open("./database/users.json", 'r') as f:
        users = json.load(f);
    
    name = request.form.get("user-name")
    password = request.form.get("password")

    if name in users and password == users[name]:
        return redirect("/bill")
    else:
        print(name)

        return redirect("/login-fom")

@app.route("/signup",methods=["POST"])
def signup():
    name = request.form.get("user-name")
    print(name)
    password = request.form.get("password")
    confirm_password = request.form.get("confirm-password")

    if password == confirm_password:

        with open("./database/users.json", 'r') as f:
            users = json.load(f);

        users[name] = password;
        print(users)

        with open("./database/users.json", 'w') as f:
            json.dump(users,f)
        mkdir("./database/"+name)
        return redirect("/bill?user=" + name)

    else:
        return redirect("/signup-form")
    
        

@app.route("/bill")
def bill_form():
    return render_template("bill.html")

@app.route("/create_bill", methods=["GET", "POST"])
def create_bill():
    with open("./database/bill_data.json", 'r') as f:
        all_bill = json.load(f)

    ths_bill = []

    for i in range(1,math.floor(len(request.form)/3)+1):
       this_bill.append({"item" : request.form.get("item-" + str(i)), "quntaty" : request.form.get("quntaty-" + str(i)), "price" : request.form.get("price-" +str(i))})

    all_bill.append(this_bill);

    with open("./database/bill_data.json", 'w') as f:
       json.dump(all_bill, f, indent=4)

    return redirect("/index")

@app.route("/stock_report")
def stock_report():
    with open("./database/bill_data.json", 'r') as f:
        bill_data = json.load(f);
    return render_template("stock_report.html", ALL_BILL=bill_data);
