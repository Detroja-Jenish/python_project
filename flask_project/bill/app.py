# write variable in upper case if that is used in templates
# use variable in uppercase in templates
from flask import Flask, render_template, redirect, request
import json
import math
from os import mkdir
from pdf import mypdf
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

        with open("./database/" + user_name.upper() + "/stock.json", 'w') as f:
        	json.dump({},f,indent=4)

        return redirect("/bill?user=" + user_name)

    else:
        return redirect("/signup-form")
    
        

@app.route("/bill")
def bill_form():
    user_name = request.args.get("user")

    with open("./database/" + user_name.upper() + "/customerAddress.json", 'r') as f:
        customers_ = json.load(f).keys();
    return render_template("bill.html", user=user_name, customers = customers_)

@app.route("/stock", methods=["GET", "POST"])
def stock():
    user_name = request.args.get("user")
    stock = {}
    
    with open("./database/" + user_name.upper() + "/stock.json", 'r') as f:
        stock = json.load(f)

    for i in range (1, len(request.form)//3 + 1):
        item =  request.form.get("item-" + str(i))
        quntaty = request.form.get("quntaty-" + str(i))
        price = request.form.get("price-" +str(i))
        
        stock[item] = {"item" : item, "quntaty" : quntaty, "price" : price}

@app.route("/create_bill", methods=["GET", "POST"])
def create_bill():
    user_name = request.args.get("user")
    this_bill = []
    all_bills = []
    stock = {}

    with open("./database/" + user_name.upper() + "/stock.json", 'r') as f:
        stock = json.load(f)

    with open("./database/" + user_name.upper() + "/bill_data.json", 'r') as f:
        all_bills = json.load(f)

    for i in range(1,math.floor(len(request.form)/3)+1):
        if( request.form.get("quntaty-" + str(i))!= ""):
            item =  request.form.get("item-" + str(i))
            quntaty = request.form.get("quntaty-" + str(i))
            price = request.form.get("price-" +str(i))
            amount = int(price)*int(quntaty);

       # stock[item][quntaty] -= quntaty
        this_bill.append({"item" : item, "quntaty" : quntaty, "price" : price, "amount" : str(amount)})

    all_bills.append(this_bill);
    cb = mypdf();
    cb.write(this_bill);
    cb.save(user_name.upper());


    with open("./database/" + user_name.upper() + "/bill_data.json", 'w') as f:
       json.dump(all_bills, f, indent=4)

    return redirect("/bill?user="+user_name)

@app.route("/sell_report")
def sell_report():
    user_name = request.args.get("user")
    with open("./database/" + user_name.upper() + "/bill_data.json", 'r') as f:
        all_bills = json.load(f)
    return render_template("sell_report.html", ALL_BILLS=all_bills, user=user_name);
    #return ("Hello")

@app.route("/get_stock_data")
def give_stock_data():
    user_name = request.args.get("user")
    stock = {}
    with open("./database/" + user_name.upper() + "/stock.json", 'r') as f:
        stock = json.load(f)

    return (stock)

@app.route("/addCustomer")
def addCustomer():
    user_name = request.args.get("user")
    return render_template("addCustomer.html", user=user_name)

@app.route("/addCustomerToDatabase", methods=["GET","POST"])
def addCustomerToDatabase():
    user_name = request.args.get("user")
    with open("./database/" + user_name.upper() + "/customerAddress.json", 'r') as f:
        all_address = json.load(f);

    cName = request.form.get("companyName");
    Building_no= request.form.get("building-no")
    street = request.form.get("street")
    landMark= request.form.get("landMark")
    zipCode = request.form.get("zipCode")
    state = request.form.get("state")
    all_address[cName] = [ cName, Building_no, street, landMark, zipCode, state]
    #all_address.append( new_address )

    with open("./database/" + user_name.upper() + "/customerAddress.json", 'w') as f:
        json.dump(all_address, f, indent=4)
    #print(new_address)
    #print(type(new_address))
    print(all_address);
    return redirect("addCustomer?user="+user_name)
