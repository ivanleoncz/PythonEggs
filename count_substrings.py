#!/usr/bin/python3

def count_substring(string, sub_string):
    init = 0  # range start, always incrementing
    counter = 0
    # range() stop == limit - 1 (start from 0)
    # last index   == limit + 1
    limit = len(string) - len(sub_string)
    for i in range(init, limit + 1): # init -> last_index
        chars = []
        chars.append(string[i]) # append the iterated char
        nxt = 0 
        # next chars based on sub_string length
        # How many chars do I have to advance on string?
        for j in range(1, len(sub_string)): 
            nxt += 1 # increments next char index
            s = string[i + nxt] # current char + next chars
            chars.append(s)
        # generating current subtring, considering the current string char + next chars    
        sub = ''.join(chars) 
        if sub == sub_string: # current substring == sub_string param
            counter += 1 # sums the substring occurrence
        init += 1 # moves the range start to the next char
    return counter

string = "ABCDCDC"
sub_string = "CDC"

print(count_substring(string,sub_string))
