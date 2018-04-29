#!/usr/bin/python3

l = []

num = int(input("Insert an int number: "))

for n in range(1, num):
    l.append(n)

print("Number between 0 and {0}: {1}".format(num, l))
