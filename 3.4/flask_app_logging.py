#/usr/bin/env python3
""" Demonstration of logging feature for a Flask App. """

from logging.handlers import RotatingFileHandler
from flask import Flask, request, jsonify
from time import strftime

__author__ = "@ivanleoncz"

import logging
import traceback


app = Flask(__name__)

@app.route("/")
@app.route("/index")
def get_index():
    """ Route for / and /index. """
    return "Welcome to Flask! "


@app.route("/data")
def get_data():
    """ Route for /data. """
    data = {
            "Name":"Ivan Leon",
            "Occupation":"Software Developer",
            "Technologies":"[Python, Flask, JavaScript, Java, SQL]"
    }
    return jsonify(data)


@app.route("/error")
def get_nothing():
    """ Route for intentional error. """
    return non_real_variable # intentional non existent variable


@app.after_request
def after_request(response):
    """ Logging after every request. """
    # This avoids the duplication of registry in the log,
    # since that 500 is already logged via @app.errorhandler.
    if response.status_code != 500:
        ts = strftime('[%Y-%b-%d %H:%M]')
        logger.error('%s %s %s %s %s %s',
                      ts,
                      request.remote_addr,
                      request.method,
                      request.scheme,
                      request.full_path,
                      response.status)
    return response


@app.errorhandler(Exception)
def exceptions(e):
    """ Logging after every Exception. """
    ts = strftime('[%Y-%b-%d %H:%M]')
    tb = traceback.format_exc()
    logger.error('%s %s %s %s %s 5xx INTERNAL SERVER ERROR\n%s',
                  ts,
                  request.remote_addr,
                  request.method,
                  request.scheme,
                  request.full_path,
                  tb)
    return "Internal Server Error", 500

if __name__ == '__main__':
    # maxBytes to small number, in order to demonstrate the generation of multiple log files (backupCount).
    handler = RotatingFileHandler('app.log', maxBytes=10000, backupCount=3)
    # getLogger('__name__'): decorators loggers to file + werkzeug loggers to stdout
    # getLogger('werkzeug'): werkzeug loggers to file + nothing to stdout
    logger = logging.getLogger('__name__')
    logger.setLevel(logging.ERROR)
    logger.addHandler(handler)
    app.run(host="127.0.0.1",port=8000)



### log ###
#
#    [2017-Aug-09 01:51] 127.0.0.1 GET http /? 200 OK
#    [2017-Aug-09 01:51] 127.0.0.1 GET http /data? 200 OK
#    [2017-Aug-09 01:51] 127.0.0.1 GET http /error? 5xx INTERNAL SERVER ERROR
#    Traceback (most recent call last):
#    File "/home/ivanlmj/git/env_flask_templates/lib/python3.4/site-packages/flask/app.py", 
#        line 1612, in full_dispatch_request
#    rv = self.dispatch_request()
#    File "/home/ivanlmj/git/env_flask_templates/lib/python3.4/site-packages/flask/app.py", 
#        line 1598, in dispatch_request
#    return self.view_functions[rule.endpoint](**req.view_args)
#    File "test.py", line 26, in get_json
#    return non_real_variable # <--------------------------------------------- intentional
#    NameError: name 'non_existent_variable' is not defined
#
###########

# Here: https://stackoverflow.com/questions/14037975/how-do-i-write-flasks-excellent-debug-log-message-to-a-file-in-production/39284642#39284642
