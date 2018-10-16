""" Generating a new Tuple based on even indexes from another Tuple as input.
"""

__author__ = "@ivanleoncz"

def oddTuples(aTup):
    '''
    aTup: a tuple
    
    returns: tuple, every other element of aTup. 
    '''
    newTup = ()
    # Your Code Here
    for idx in range(0, len(aTup)):
        if idx % 2 == 0:
            newTup += (aTup[idx], )
    return newTup

print(oddTuples((3, 9, 14, 7, 19, 3, 20)))
# expected result: (3, 14, 19, 20)
