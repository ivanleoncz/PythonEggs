#!/usr/bin/python3

names = ["julian", "alfred", "monica", "atlas", "mariane", "leyla", "angeline"]

even_indexes = [i for i in names if names.index(i) % 2 == 0]

print("\nNames:", names)
print("Names from even indexes:", even_indexes)
