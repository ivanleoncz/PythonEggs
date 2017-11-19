#!/usr/bin/python3

from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def f_index():
    ua = request.headers.get('User-Agent')
    return "<h2> User-Agent: </h2> %s" % ua

if __name__ == "__main__":
    app.run(host="0.0.0.0")
