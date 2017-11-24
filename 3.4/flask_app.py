#!/usr/bin/python3

from flask import Flask

app = Flask(__name__)

@app.route("/")
def f_index():
    return "Welcome to Flask!"

if __name__ == "__main__":
    app.run()
