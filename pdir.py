#!/usr/bin/python3
""" Demonstrates the usage of dir(), with better output. """

__author__ = "ivanleoncz"

obj = "I am a string."
count = 0

print("\nObject Data: ", obj)
print("Object Type: ", type(obj),"\n")

for method in dir(obj):
    # the end=" " at the end of the print statement, 
    # makes it printing in the same line, 4 times (count)
    print("|    {:20}".format(method), end=" ")
    count += 1
    if count == 4:
        count = 0
        print("") 
