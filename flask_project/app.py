from flask import Flask, request, render_template, redirect;
from flaskext.mysql import MySQL

app = Flask( __name__ )
mysql = MySQL()
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'jen@2004'
app.config['MYSQL_DATABASE_DB'] = 'lab9'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)

conn = mysql.connect()

cursor = conn.cursor();

@app.route("/")
def index():
    cursor.execute("describe city")
    data = cursor.fetchall();
    print(data);
    return "hello world"
