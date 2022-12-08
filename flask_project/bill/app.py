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
    
    user_name = request.form.get("user-name")
    password = request.form.get("password")

    if user_name in users and password == users[user_name]:
        return redirect("/bill?user=" + user_name)
    else:
        pass

        return redirect("/login-fom")

@app.route("/signup",methods=["POST"])
def signup():
    user_name = request.form.get("user-name")
    print(name)
    password = request.form.get("password")
    confirm_password = request.form.get("confirm-password")

    if password == confirm_password:

        with open("./database/users.json", 'r') as f:
            users = json.load(f);

        users[user_name] = password;
        print(users)

        with open("./database/users.json", 'w') as f:
            json.dump(users,f)
            
        mkdir("./database/"+user_name.upper())
        
        with open("./database/" + user_name.upper() + "/bill_data.json", 'w') as f:
        	json.dump([],f,indent=4)
        return redirect("/bill?user=" + name)

    else:
        return redirect("/signup-form")
    
        

@app.route("/bill")
def bill_form():
    user_name = request.args.get("user")
    return render_template("bill.html", user=user_name)

@app.route("/create_bill", methods=["GET", "POST"])
def create_bill():
    user_name = request.args.get("user")
    this_bill = []
    all_bills = []
    
    with open("./database/" + user_name.upper() + "/bill_data.json", 'r') as f:
        all_bills = json.load(f)

    for i in range(1,math.floor(len(request.form)/3)+1):
       this_bill.append({"item" : request.form.get("item-" + str(i)), "quntaty" : request.form.get("quntaty-" + str(i)), "price" : request.form.get("price-" +str(i))})

    all_bills.append(this_bill);

    with open("./database/" + user_name.upper() + "/bill_data.json", 'w') as f:
       json.dump(all_bills, f, indent=4)

    return redirect("/bill?user="+user_name)

@app.route("/stock_report")
def stock_report():
    user_name = request.args.get("user")
    with open("./database/" + user_name.upper() + "/bill_data.json", 'r') as f:
        all_bills = json.load(f)
    return render_template("stock_report.html", ALL_BILL=all_bills, user=user_name);
