#!/usr/bin/python3

from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def f_index():
    ua = request.headers.get('User-Agent')
    if "Windows Phone" in ua:
        return "Hello, Windows Phone!"
    elif "Android" in ua:
        return "Hello, Android!"
    elif "iPad" in ua:
        return "Hello, iPad!"
    elif "iPhone" in ua:
        return "Hello, iPhone!"
    elif "Windows NT" in ua:
        return "Hello, Windows!"
    elif "X11" in ua:
        return "Hello, GNU/Linux!"
    elif "Mac OS X":
        return "Hello, Macintosh!"
    else:
        return "I don't know you..."

if __name__ == "__main__":
    app.run(host="0.0.0.0")
