#!/usr/bin/python3
""" Demonstrating the usage of assertions (sanity-check). """

__author__ = "@ivanleoncz"


def check_options(opt1, opt2, op3):

    try:
        assert type(opt1) is str, "opt1 is not a string."
        assert type(opt2) is str, "opt2 is not a string."
        assert type(opt3) is str, "opt3 is not a string."
        return "OK"
    except AssertionError as e:
        print(e)
        return "NOK"


print(check_options(4, "--create", 45))

