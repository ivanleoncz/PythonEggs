#!/usr/bin/python3
""" Strings in a Nutshell. """

s = "Sweet Home Alabama Festival"

print("\n",s,"\n")
print("- string length:\033[1;32m", len(s), "\033[1;m")
print("- counting letter 'a':\033[1;32m",s.count("a"), "\033[1;m")
print("- first index for letter 'a':\033[1;32m", s.find("a"), "\033[1;m")
print("- lowercase:\033[1;32m", s.lower(), "\033[1;m")
print("- uppercase:\033[1;32m", s.upper(), "\033[1;m")
print("- split into substrings:\033[1;32m", s.split(), "\033[1;m")
print("- all alphabetic chars? \033[1;32m", s.isalpha(), "\033[1;m")
print("- all alphanumeric char? \033[1;32m", s.isalnum(), "\033[1;m")
print("- all numeric chars? \033[1;32m", s.isdigit(), "\033[1;m")

