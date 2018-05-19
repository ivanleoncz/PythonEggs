#!/usr/bin/python3
""" Determining Valid Passwords: plain text VS hashed.

    You can use this concept for storing hashed passwords
    on a DB and later on, making this type of procedure on
    your code, in order to determine a successful login.
"""

import bcrypt
from getpass import getpass


def encrypt(p):
    """
        Concept:
            Encrypts plain text password into a hash.

        Parameter:
            p: Plain text password.

        Return:
            Plain text password encrypted.
    """
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(p.encode('utf-8'), salt)
    return hashed


def validate(p, hashed):
    """
        Concept:
            Validates password, generating a new hash, using the
            provided hash as salt value and comparing the provided
            hash VS the new hash.

        Parameters:
            p: Plain text password.
            hashed: Generated hash, based on plain text password.

        Return:
            True: if hashed and new_hash are equal.
            False: if hashed and new_hash are not equal.
    """
    new_hash = bcrypt.hashpw(p.encode('utf-8'), hashed)
    if hashed == new_hash:
        return True
    else:
        return False
