#!/usr/bin/python3
""" Demonstrating Flask, using a APScheduler. """

from apscheduler.schedulers.background import BackgroundScheduler
from flask import Flask

def sensor():
    """ Function for test purposes. """
    print("Scheduler is alive!")

sched = BackgroundScheduler(daemon=True)
sched.add_job(sensor,'interval',seconds=60)
sched.start()

app = Flask(__name__)

@app.route("/")
def home():
    """ Route for test purposes. """
    return "Flask says: Hello !"

if __name__ == "__main__":
    app.run()


