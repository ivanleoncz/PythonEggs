#!/usr/bin/python3

def gcdRecur(a, b):
    # Base case is when b = 0
    print("\n * value A:", a)
    print(" * value B:", b)
    if b == 0:
        return "\nGDC: %s" % a
    # Recursive case
    print(" * recursion: ({0}, {1} % {2})".format(b,a,b))
    return gcdRecur(b, a % b)

print("\nValues: (6,21)")
print(gcdRecur(6,21))
