#!/usr/bin/python3

""" Testing lambda functions. """


n = int(input("Insert a number, please: "))

f = lambda x, y : x * y
res = f(2,n)

print("Number multiplied by 2: ",res)

