#!/usr/bin/python3
""" Initializing SQLite3 Database. """


import sqlite3
import bcrypt
from getpass import getpass

dbfile = "app_users.lite"
db     = sqlite3.connect(dbfile)
cursor = db.cursor()
table  = "users"


def create_table_user():
    """ Creating table and the first user. """

    # local variables for user creation
    name     = "Dennis Ritchie"
    country  = "USA"
    username = "dennis@unix.com"

    # hashing password
    salt = bcrypt.gensalt()
    password = "us3rp4ss".encode("utf-8")
    passhash = bcrypt.hashpw(password,salt)
    passhash = passhash.decode("utf-8")
 
    # queries
    dropif = "DROP TABLE IF EXISTS {0}".format(table)
    cursor.execute(dropif)
    create = """ CREATE TABLE '{0}' (id INTEGER PRIMARY KEY, name TEXT, 
                 country TEXT, username TEXT UNIQUE, password TEXT); 
             """.format(table)
    cursor.execute(create)
    insert = """ INSERT INTO '{0}' (id,name,country,username,password) 
                 VALUES (1,'{1}','{2}','{3}','{4}');
             """.format(table,name,country,username,passhash)
    cursor.execute(insert)
    db.commit()
    return None


def validate_table():
    select = "SELECT name FROM sqlite_master WHERE type = 'table' and name = '{0}';".format(table)
    cursor.execute(select)
    db.commit()
    data = cursor.fetchall()
    return data


def validate_user_pass(username,password):
    """ Password validation. """
    select = "SELECT password FROM '{0}' WHERE username = '{1}';".format(table,username)
    cursor.execute(select)
    db.commit()
    salt = cursor.fetchone()
    if salt is not None:
        salt = salt[0].encode("utf-8")
        hashsalt = bcrypt.hashpw(password,salt)
        if hashsalt == salt:
            return 0
        else:
            return 1
    else:
        return 2


if __name__ == "__main__":
    """ When used as script. """
    data = validate_table() # validates if table already exists
    if len(data) == 0:
        print("\n  * Notice: Table and First User successfully created.\n")
        create_table_user()
    username = input("Username: ") # proceeding normal execution
    password = getpass(prompt="Password: ").encode("utf-8")
    validation = validate_user_pass(username,password)
    if validation == 0:
        print("\n  * Username: OK / Password: OK\n")
    elif validation == 1:
        print("\n  * Username: OK / Password: NOK\n")
    elif validation == 2:
        print("\n  * Username: Not Found!\n")
