from math import pi,tan

def polysum(n,s):
    perim = 0
    for side in range(n):
        perim += s
        area = 0.25*n*(s**2) / tan( pi/n )
    result = area + perim ** 2
    return round(result, 4)

print(polysum(n,s))
