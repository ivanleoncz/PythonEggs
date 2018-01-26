#!/usr/bin/python3
""" Transforms string into a list in alphabetical order."""

string = "sdioajdansiaosfasfa"
print("String:",string)

l = list(string)
l.sort()
print("String Alphabet:",l)

l_unique = list(set(l))
l_unique.sort()
print("String Alphabet Unique:",l_unique)
