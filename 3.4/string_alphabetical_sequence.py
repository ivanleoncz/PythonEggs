#!/usr/bin/python3
""" Transforms string into a list in alphabetical order."""

import json

s = "sdioajdansiaosfasfa"
print("\nString:", s)

l = list(s)
l.sort()
l_unique = list(set(l))
l_unique.sort()
print("Alphabetic Order (Unique):",l_unique)

alpha_dict = {}
idx = 0
for l in l_unique:
    alpha_dict[idx] = l
    idx += 1

print("Alphabet with Indexes:\n\n",json.dumps(alpha_dict, indent=4))
