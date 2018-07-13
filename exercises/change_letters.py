#!/usr/bin/python3

import string

def LetterChanges(s):
    print("Input:", s)
    alphabet = list(string.ascii_lowercase)
    str_list = list(s)
    for char in list(s):
        if char in string.punctuation or char in string.digits or char == ' ':
            pass
        else:
            str_index   = str_list.index(char)
            alpha_index = alphabet.index(char)
            next_letter = alphabet[alpha_index + 1]
            str_list.remove(char)
            if next_letter == 'z':
                str_list.insert(str_index, 'a')
            elif next_letter in "aeiou":
                str_list.insert(str_index, next_letter.upper())
            else:
                str_list.insert(str_index, next_letter)

    s = "".join(str_list)
    return "Ouput: %s" % s


print(LetterChanges("hello*3"))
print(LetterChanges("fun times!"))

