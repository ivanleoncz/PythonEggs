#!/usr/bin/python3

""" Calculates the number of times the word 'bob'

appears on the 'string' variable.
"""

string = "azcbobobegghakl"
count = 0
l1 = "a"
l2 = "a"
l3 = "a"

for letter in string:
    l1 = l2
    l2 = l3
    l3 = letter
    word = l1 + l2 + l3
    if word == "bob":
        count += 1

print("Number of time bob occurs is: ", count)
