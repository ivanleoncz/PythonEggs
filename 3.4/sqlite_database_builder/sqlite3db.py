#!/usr/bin/python3
''' Initializing SQLite3 Database. '''

import sqlite3

db       = sqlite3.connect('app_users.lite')
cursor   = db.cursor()
table    = "users"

name     = "Dennis Ritchie"
country  = "USA"
email    = "dennis@unix.com"
password = "us3rp4ss"

def create_table():
    drop = "DROP TABLE IF EXISTS {0}".format(table)
    cursor.execute(drop)
    create = "CREATE TABLE {0} (id INTEGER PRIMARY KEY, name TEXT, country TEXT, email TEXT UNIQUE, password TEXT);".format(table)
    cursor.execute(create)
    db.commit()
    return None

def create_user():
    insert = "INSERT INTO {0} (id,name,country,email,password) VALUES(1,'{1}','{2}','{3}','{4}');".format(table,name,country,email,password)
    cursor.execute(insert)
    db.commit()
    return None

create_table()
create_user()
