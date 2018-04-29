#!/usr/bin/python3
""" Pretty dir() output. """

__author__ = "ivanleoncz"

def run(data):
    count = 0
    for method in dir(data):
        # end=" " -> prints in the same line
        print("| {:>20}".format(method), end=" ")
        count += 1
        # ...for four times only
        if count == 4:
            count = 0
            print("")
