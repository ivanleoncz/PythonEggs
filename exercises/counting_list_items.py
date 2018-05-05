#!/usr/bin/python3

d = {}

fruits = ["banana", "apple", "cherry", "apple", "orange", "banana", "cherry"]
for f in fruits:
    if d.get(f):
        d[f] += 1
    else:
        d[f] = 1

print("\nFruits:", fruits)
print("Counting:", d, "\n")
