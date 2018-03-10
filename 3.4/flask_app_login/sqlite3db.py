#!/usr/bin/python3
""" Module for SQLite3 Database setup and operation. """

import sqlite3
import bcrypt
from getpass import getpass


class Database:

    dbfile = "users_db.lite"
    db     = sqlite3.connect(dbfile)
    cursor = db.cursor()
    table  = "users"

    def create_table_user(self):
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
        dropif = "DROP TABLE IF EXISTS {0}".format(self.table)
        self.cursor.execute(dropif)
        create = """ CREATE TABLE '{0}' (id INTEGER PRIMARY KEY, name TEXT, 
                     country TEXT, username TEXT UNIQUE, password TEXT); 
                 """.format(self.table)
        self.cursor.execute(create)
        insert = """ INSERT INTO '{0}' (id,name,country,username,password) 
                     VALUES (1,'{1}','{2}','{3}','{4}');
                 """.format(self.table,name,country,username,passhash)
        self.cursor.execute(insert)
        self.db.commit()
        return None


    def validate_table(self):
        """ Validates the existence of users table. """
        select = """ SELECT name FROM sqlite_master 
                     WHERE type = 'table' and name = '{0}';
                 """.format(self.table)
        self.cursor.execute(select)
        self.db.commit()
        data = self.cursor.fetchall()
        return data


    def validate_user_pass(self,username,password):
        """ Password validation. """
        select = """ SELECT password FROM '{0}' 
                     WHERE username = '{1}';
                 """.format(self.table,username)
        self.cursor.execute(select)
        self.db.commit()
        salt = self.cursor.fetchone()
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
    """ For usage as script. """
    database = Database()
    data = database.validate_table()
    if len(data) == 0: # if users table exists
        database.create_table_user()
        print("\n  * Notice: Table + First User successfully created.\n")
    username = input("Username: ") # following normal execution
    password = getpass(prompt="Password: ").encode("utf-8")
    validation = database.validate_user_pass(username,password)
    if validation == 0:
        print("\n  * Username: OK / Password: OK\n")
    elif validation == 1:
        print("\n  * Username: OK / Password: NOK\n")
    elif validation == 2:
        print("\n  * Username: Not Found!\n")
