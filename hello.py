from flask import Flask,render_template, request, redirect, url_for, session
from flask import *
from fileinput import filename
import json
import pymongo
import os
import matplotlib.pyplot as plt
from io import BytesIO
import base64

contains_emails=[]

app = Flask(__name__)
myclient=pymongo.MongoClient("mongodb://localhost:27017/")
mydb= myclient["mydatabase"]
mycol = mydb["email"]
myhire= mydb["hire"]

@app.route('/')
def hello():
    return render_template("front_page.html")


@app.route('/success', methods=['POST'])
def success():
    if request.method == 'POST':
        f = request.files['file']
        f.save(f.filename)
        print(f.filename)
        return render_template("acknowledgement.html", name=f.filename)

@app.route('/index')
def inde():
    return render_template("index.html")

@app.route("/starttest")
def start():
    return render_template("start.html")

@app.route("/regester")
def regester():
    return render_template("regester.html")

# @app.route("/test",methods=['POST'])
# def test():
#     return render_template("test.html")

@app.route("/submit",methods=['POST'])
def submit():
    answers = {}
    for key, value in request.form.items():
        if key.startswith('q'):
            question_number = key[1:]
            answers[question_number] = value

    print("User submitted answers:", answers)

    return "Form submitted successfully"



@app.route('/register', methods=['POST'])
def register():
    email = request.form.get('email')
    password = request.form.get('password')
    mydict = {"email": email, "password": password}
    x = mycol.insert_one(mydict)
    return render_template("regester.html")

@app.route('/login')
def lo():
    return render_template("login.html")

@app.route('/logins',methods=['POST'])
def login():
    email = request.form.get('email')
    password = request.form.get('password')
    mydb = myclient["mydatabase"]
    mycol = mydb["email"]
    mydict = {"email": email}
    x = mycol.find(mydict)
    print(email)
    print(password)
    try:
        y = x[0]
        print(y['email'])
        print(y['password'])
        if y['email'] == email and y['password'] == password:
            return render_template("fileupload.html")
        else:
            return "ah ah !"
    except:
        return "ah ah gothca!"



@app.route('/hirelogin', methods=['POST'])
def hirelogin():
    email = request.form.get('email')
    password = request.form.get('password')
    mydb = myclient["mydatabase"]
    myhire = mydb["hire"]

    appl = mydb["email"]
    applicants = appl.find()
    count = 0
    l=[]
    for j in applicants:
        count += 1
        l.append(j['email'])
        print(j['email'])

    mydict = {"email": email}
    x = myhire.find(mydict)

    try:
        y = x[0]
        if y['email'] == email and y['password'] == password:
            return render_template("home.html",applicants=l)
        else:
            return "ah ah !"
    except:
            return "ah ah gothca!"


@app.route('/hireregister', methods=['POST'])
def rehiregister():
    email = request.form.get('email')
    password = request.form.get('password')
    mydict = {"email": email, "password": password}
    myhire=mydb["hire"]

    x = myhire.insert_one(mydict)
    appli = mydb["email"]

    return "Hirer successfully logged in"

@app.route("/hireregister")
def regi():
    return render_template("hireregister.html")

@app.route("/hirelogin")
def hirelogins():
    return render_template("hirelogin.html")

@app.route("/chinmay_home")
def chin():
    return render_template("chinmay_home.html")

@app.route("/test")
def test():
    return render_template("test.html")