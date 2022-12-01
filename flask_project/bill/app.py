from flask import Flask, render_template, redirect, request
import json
import math

app = Flask("__name__")
@app.route("/")
def index():
    return render_template("bill.html")
@app.route("/create_bill", methods=["GET", "POST"])
def create_bill():
    final = {}

    for i in range(1,math.floor(len(data)/3)+1):
        final[i] = {"item" : request.form.get("item-" + str(i)), "qntaty" : request.form.get("quntaty-" + str(i)), "price" : request.form.get("price-" +str(i))}
    with open("bill_data.json", 'w') as f:
       json.dump(final, f, indent=4)
    print(data)
    print(type(len(data)/3))

    return redirect("/")
