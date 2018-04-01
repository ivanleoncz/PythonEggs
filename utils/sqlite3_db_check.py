#!/usr/bin/python3
""" Verifies the existence of a SQLite3 database file. """

__author__ = "@ivanleoncz"

import os
import sys


def sqlite3_check():
    db_filename = input("Database filename (end with .sqlite3):")
    if os.path.isfile(db_filename) and os.path.getsize(db_filename) > 100:
        with open(db_filename,'r', encoding = "ISO-8859-1") as f:
            header = f.read(100)
            if header.startswith('SQLite format 3'):
                return "INFO: database file has been detected."
            else:
                return "ERROR: NO database file has been found."


print(sqlite3_check())
