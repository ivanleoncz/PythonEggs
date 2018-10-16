#!/usr/bin/python3
""" Printing a staircase. """

hashtag = "#"
step = 10

print("\n[STAIRCASE]\n")
for i in reversed(range(step)):
    print('{0:>{1}}'.format(hashtag,step))
    hashtag += "#"

