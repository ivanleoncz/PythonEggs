#!/usr/bin/python3
""" Encrypting and validating passwords."""

from getpass import getpass

__author__ = "@ivanleoncz"

import bcrypt

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

"""
def generate():

    import string
    import random

    chars = string.ascii_uppercase + string.ascii_lowercase + string.punctuation + string.digits
    print(chars)
    print("".join(random.choice(chars) for step in range(10)))
    print("".join(random.choice(chars) for step in range(10)))
"""
