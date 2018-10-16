#!/usr/bin/python3

d = {}

fruits = ["banana", "apple", "cherry", "apple", "orange", "banana", "cherry"]
for f in fruits:
    d[f] = fruits.count(f)

print("\nFruits:", fruits)
print("Counting:", d, "\n")
