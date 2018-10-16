# edX Grader automatically provides a string as input
# s = input()

word = ""

substrings = []                                                                 
last_char  = "a"                                                                
sub_string = ""                                                                 
                                                                                
for c in s:                                                                     
    if c >= last_char:                                                          
        sub_string += c                                                         
        last_char   = c
        substrings.append(sub_string) 
    else:                                                                                                                 
        last_char  = c                                                        
        sub_string = c                                                         

answer = max(substrings, key=len)

print("Longest string in alphabetical order is:", answer)
