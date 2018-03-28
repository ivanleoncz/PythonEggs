""" Calculates the sum of the area and the square of the perimeter from a
regular polygon.
"""
from math import pi,tan

__author__ = "@ivanleoncz"

def polysum(n,s):
    """ n: number of sides of the polygon
        s: length of each side

        returns: area + (square of the perimeter)
    """
    perim = 0
    for side in range(n):
        perim += s
    area = 0.25*n*(s**2) / tan( pi/n )
    result = area + perim ** 2
    return round(result, 4)

print(polysum(n,s))
