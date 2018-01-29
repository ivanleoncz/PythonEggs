#!/usr/bin/python3

import sqlite3

db = sqlite3.connect('sample_db.lite')
cursor = db.cursor()
table = "users"
user = "Dennis Ritchie"
email = "dennis@unix.com"
country = "USA"

def check_table():
    query = "SELECT name FROM sqlite_master WHERE type = 'table' and name = '{0}';".format(table)
    cursor.execute(query)
    db.commit()
    check = cursor.fetchall()
    return check

def create_table():
    query = "CREATE TABLE {0} (id INTEGER PRIMARY KEY, name TEXT, email TEXT unique, country TEXT);".format(table)
    cursor.execute(query)
    db.commit()
    return None

def create_user():
    query = "INSERT INTO {0} (id,name,email,country) VALUES(1,'{1}','{2}','{3}');".format(table,user,email,country)
    cursor.execute(query)
    return None

def find_user():
    select = "SELECT name FROM {0} WHERE name = '{1}';".format(table,user)
    cursor.execute(select)
    db.commit()
    data = cursor.fetchall()
    return data


print("Checking existence of table: {0}").format(table)
check = check_table()
if len(check) == 0:
    print("Creating table: {0}").format(table)
    create_table()
    check = check_table()
    if len(check) != 0:
        print("Creating User: {0}").format(user)
        create_user()
        data = find_user()
        if len(data) != 0:
            print("-> User successfully created!\n")
        else:
            print("User not found...")
    else:
        print("Table not found...")
else:
    print("Table {0} already exists.".format(table))
