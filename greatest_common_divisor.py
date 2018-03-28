#!/usr/bin/python3
""" Finding the Greatest Common Divisor (GDC).

If remainders of both are equal:
- than the value generated via iteration is the GDC

Else:
- a next descending step is taken in order to divide
both numbers for determining if the division 
has generated remainder 0

"""

def gcdIter(a, b):
    '''
    '''
    if a < b:
        for i in range(-a,0):
            i = abs(i)
            div_a = a % i
            div_b = b % i
            if div_a == 0 and div_b == 0:
                return i
                break
    else:
        for i in range(-b,0):
            i = abs(i)
            div_a = a % i
            div_b = b % i
            if div_a == 0 and div_b == 0:
                return i
                break
    
print(gcdIter(21, 24))        
