#!/usr/bin/python3
""" Here's the workflow of this recursive solution:

    [Factorial of 4]
    
    factorial (4): 4 not equal to 1, 4 * return factorial(4 - 1)...
    |
    ---> factorial (3): 3 not equal to 1, 3 * return factorial(3 - 1)...
         |
         ---> factorial (2): 2 not equal to 1, 2 * return factorial(2 - 1)...
              |
              ---> factorial (1): 1 is equal to 1, return 1

    At the end of every function call, 'n' waits for the result of another
    call of the same function, that receives 'n - 1' as parameter: the call
    of the same function (recursion) is performed successively, until the 
    value of 'n' is equal to 1. Until this condition is true, all other 'n'
    values are waiting for the end of the recursion, when 'n' is equal to 1.

    Therefore, the factorial of a number is obtained through Recursion.

    n = 4:

    factorial(n): x factorial(n-1) x factorial(n-1) x factorial(n-1) == 24
  
    ================================================================

    4 x factorial(4-1)
                   3 x factorial(3-1)
                                  2 x factorial(2-1)
                                                 1 == 24

    One thing to keep in mind regarding Recursion: all operations are not
    considering additional variables in order to keep a state of a calculation
    or whicever operation that might be. The point is, to work with the param
    of the function, which is modified in order to be passed to a next step of
    recursion
"""


number = int(input("Factorial of: "))

def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)


print("Result:", factorial(number))
