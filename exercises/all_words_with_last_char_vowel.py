#!/usr/bin/python3

s = "I was thinking about you and maybe, we can go out and have a juice."
print("\nString:", s, "\n")
l = s.split()

# filter: evaluating if the last char of each string is a vowel
# map: stripping characters for each item from filter iterator
result = list(
            map(lambda s: s.strip('.,') ,
                filter(lambda s: s.strip('.,')[-1] in "aeiou", l)
            )
         )
print("Result:", result)
