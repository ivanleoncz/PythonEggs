#!/usr/bin/python3

import string

lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
print("Letters Guessed:", lettersGuessed)


def getAvailableLetter(lettersGuessed):
    alphabet = list(string.ascii_lowercase)
    print("Alphabet:", alphabet)
    for c in lettersGuessed:
        alphabet.remove(c)
    return "Available: %s" % ("".join(alphabet))


print(getAvailableLetter(lettersGuessed))
