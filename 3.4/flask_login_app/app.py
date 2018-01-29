#!/usr/bin/python3

from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def f_index():
    return "\nWelcome to Flask!\n"

@app.route("/login", methods=['GET','POST'])
def f_login():
    if request.method == "GET":
        return "\nHere you can login!\n"
    elif request.method == "POST":
        return "\nWaiting for your post.\n"

if __name__ == "__main__":
    app.run()
