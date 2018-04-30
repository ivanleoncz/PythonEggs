#!/usr/bin/python3
""" Dictionaries in a Nutshell. """

countries = {
        "Denmark":"Copenhagen",
        "South Africa":"Johanesburgo",
        "Argentina":"Buenos Aires"
        }

print("\n",countries,"\n")
print("- Keys:\033[1;32m", countries.keys(), "\033[1;m")
print("- Values:\033[1;32m", countries.values(), "\033[1;m")
print("- Items:\033[1;32m", countries.items(), "\033[1;m")
print("- Capital of Denmark:\033[1;32m", countries.get("Denmark"), "\033[1;m")
countries.pop("Denmark")
print("- Denmark was removed:\033[1;32m", countries, "\033[1;m")
countries.update({"Japan":"Tokyo", "Egypt":"Cairo"})
print("- Japan and Egypt were added:\033[1;32m", countries, "\033[1;m")

print("\nIterating over items():")
for k,v in countries.items():
    print(" Key:  ",k)
    print(" Value:",v)
