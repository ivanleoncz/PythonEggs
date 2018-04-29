#!/usr/bin/python3
''' Demonstrating Python built-ins for string data type.'''

words = "The Words Of An Eternal Soul Will Remain Forever In Our Hearts."

print("\nSTRING:",words)
print("\n- numbers of ocurrences of the letter w:",words.count("W"))
print("- print all lowercase:",words.lower())
print("- print all uppercase:",words.upper())
print("- split into substrings:",words.split())
print("- returns index for the first ocurrence of the letter a:",words.find("a"))
print("- string length:",len(words))
