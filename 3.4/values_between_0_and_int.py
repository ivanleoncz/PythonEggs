#!/usr/bin/python3

s = ""
n = int(input("Insert an int number:"))
n += 1

for i in range(n):
    if i != 0:
        s = s + str(i)

print("Number between 0 and the int number: ", s)
