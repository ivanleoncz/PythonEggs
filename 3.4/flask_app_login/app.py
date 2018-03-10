#!/usr/bin/python3

""" Login application written in Python Flask. """

from flask import Flask, session, redirect, render_template, request

__version__ = "1.0"
__author__  = "ivanleoncz"

import sqlite3db

app = Flask(__name__)
app.config.from_object("config")

@app.route("/")
@app.route("/index")
def f_index():
    return redirect("/login")

@app.route("/login", methods=['GET','POST'])
def f_login():
    if request.method == "GET":
        return render_template("login.html")
    elif request.method == "POST":
        username = request.form['username']
        password = request.form['password'].encode("utf-8")
        database = sqlite3db.Database()
        login = database.validate_user_pass(username,password)
        if login == 0:
            session["username"] = username
            return redirect("/home")
        elif login == 1 or login == 2:
            fail = "Check credentials, please."
            return render_template("login.html",login_failed=fail)

@app.route("/logout")
def f_logout():
    if "username" in session:
        session.pop("username")
    return redirect("/login")

@app.route("/home")
def f_home():
    if "username" in session:
        return render_template("home.html")
    return redirect("/login")

if __name__ == "__main__":
    app.run(host="localhost",port=8000)
