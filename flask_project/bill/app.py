# write variable in upper case if that is used in templates
# use variable in uppercase in templates
from flask import Flask, render_template, redirect, request
import json
import math
from os import mkdir
from pdf import mypdf
from MyDb import MyDatabase

app = Flask("__name__")

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
        db = MyDatabase("");
        db.signUpSetup(user_name, password);
        return redirect("/bill?user=" + user_name)

    return redirect("/signup-form")
    
        

@app.route("/bill")
def bill_form():
    user_name = request.args.get("user");
    db = MyDatabase( user_name );
    return render_template("bill.html", user=user_name, customers = db.getOnlyCustomerName());

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
    #stock is baki for implitation
   
    user_name = request.args.get("user")
    db = MyDatabase(user_name);
    this_bill = [];

    for i in range(1,math.floor(len(request.form)/3)+1):
        
        if( request.form.get("quntaty-" + str(i))!= ""):
            item =  request.form.get("item-" + str(i))
            quntaty = request.form.get("quntaty-" + str(i))
            price = request.form.get("price-" +str(i))
            amount = int(price)*int(quntaty);
        
            this_bill.append({"item" : item, "quntaty" : quntaty, "price" : price, "amount" : str(amount)})

    customerName = request.form.get("customerName");
    if(customerName == None or customerName == ""):
        customerName = "Anonymous";
    db.updateBillData(this_bill, customerName);
    cb = mypdf();
    cb.write(this_bill, user_name.upper());

    return redirect("/bill?user="+user_name)

@app.route("/sell_report")
def sell_report():
    user_name = request.args.get("user")
    db = MyDatabase( user_name );

    return render_template("sell_report.html", CUSTOMERS = db.getCustomers(), ALL_BILLS = db.getBills(), user=user_name);

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
    
    db = MyDatabase( user_name );

    cName = request.form.get("companyName");
    Building_no= request.form.get("building-no")
    street = request.form.get("street")
    landMark= request.form.get("landMark")
    zipCode = request.form.get("zipCode")
    state = request.form.get("state")

    db.addCustomer(cName, [ cName, Building_no, street, landMark, zipCode, state] );
    return redirect("addCustomer?user="+user_name)

if __name__ == '__main__':
    app.run(host = '192.168.233.26' );
