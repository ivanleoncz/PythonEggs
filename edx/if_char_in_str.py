#!/usr/bin/python3
""" Verifies if string contains the char. """

def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    '''
    start = 0 # first index of string (never changes)
    end   = len(aStr)
    ans   = (start + end) // 2
    print("\nString: ", aStr)
    print("Char:   ", char)
    print("Start:  ", start)
    print("End:    ", end)
    print("Answer: ", ans)
    if ans == 0 or len(aStr) == 0:
        return False
    else:
        if char == aStr[ans]:
            return True
        elif char < aStr[ans]:
            # slicing string (from end to start)
            return isIn(char, aStr[:ans]) 
        elif char > aStr[ans]:
            # slicing string (from start to end)
            return isIn(char, aStr[ans:]) 
        else:
            return False


print(isIn("t","cilnorz"))
