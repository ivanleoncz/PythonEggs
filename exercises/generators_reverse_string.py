#!/usr/bin/python3

def rev_str(my_str):
    length = len(my_str)
    for i in range(length -1, -1, -1):
        yield my_str[i]

s = "Hello"
print("String:", s)
print("...reversing...")

for char in rev_str("Hello"):
    print(char)


