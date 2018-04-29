#!/usr/bin/python3
""" Determining Valid Passwords: plain text VS hashed.

    You can use this concept for storing hashed passwords
    on a DB and later on, making this type of procedure on
    your code, in order to determine a successful login.
"""

import bcrypt
from getpass import getpass

# hashed password
salt = bcrypt.gensalt()
password = "mysecret".encode('utf-8')
password_hashed = bcrypt.hashpw(password,salt)

# unhashed password
# plain: the salt value is stored at the beggining of the password hash
password = getpass(prompt="Please, insert the password: ").encode('utf-8')
password_unhashed = bcrypt.hashpw(password,password_hashed)

if password_hashed == password_unhashed:
    print True
else:
    print False
