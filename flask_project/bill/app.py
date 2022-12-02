# write variable in upper case if that is used in templates
# use variable in uppercase in templates
from flask import Flask, render_template, redirect, request
import json
import math

app = Flask("__name__")

all_bill = []
this_bill = []

@app.route("/index")
def index():
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
