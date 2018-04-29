#!/usr/bin/python3
""" Prints a string in Alphabetical Order. """

s = "wsedjchausthndjsoal"
print("String:", s)

l = list(s)
l.sort()
print("Alphabetical Order",''.join(l))

