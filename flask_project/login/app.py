from flask import Flask, render_template, request, redirect
import json

app = Flask(__name__, static_url_path="/static");

with open("./user_data.json", 'r') as f:
    users = json.load(f);

@app.route("/")
def index():
    if "flag" in request.args:
        return render_template("index.html", flag=1, message="user-name or password is invalid");
    return render_template("index.html", flag=1, message="hello my name is Jenish Detroja ");

@app.route("/greet", methods=["Get", "POST"])
def greet():
    name = request.form.get("user-name", "anoumys").capitalize();
    if name in users:
        print(request.form);
        print( users[name]["user-password"] );
        print(request.form.get("password"))
        if users[name]["user-password"] == (request.form.get("password")):
            return render_template("greet.html",img_src="/static/" + users[name]["user-name"] + ".jpg", name=name);
        else:
            return redirect("/index?flag=1");
    else:
        return redirect("/?flag=1");

@app.route("/register", methods=["GET", "POST"])
def new_user():
    if request.method == "GET":
        return render_template("register.html")
    else:
        if(request.form.get("user-name", "none") != "none") and (request.form.get("password") == request.form.get("confirm-password")):
            users[request.form.get("user-name").capitalize()] = { "user-name" : request.form.get("user-name").capitalize(), "user-password" : request.form.get("password"), "src" : "/static/" + request.form.get("user-name").capitalize() + ".jpg"}
            print(users);

       #else part in incomplete and it will be for redirecting same page or throw error

        with open("./user_data.json", 'w') as f:
           json.dump(users, f, indent=4);

        return render_template("greet.html", img_src=users[request.form.get("user-name").capitalize()]["src"], name=users[request.form.get("user-name").capitalize()]["user-name"])
        
        #return (request.form.get("name"))
