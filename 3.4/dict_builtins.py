#!/usr/bin/python3
''' Demonstrating Python built-ins for dict data type. '''

countries = {"Denmark":"Copenhagen","South Africa":"Johanesburgo","Argentina":"Buenos Aires"}

print("\nDICTIONARY:",countries)
print("\n- get keys:",countries.keys())
print("- get values:",countries.values())
print("- get keys and values:",countries.items())
print("- get value from key 'Denmark':",countries.get("Denmark"))
print("- get value from key 'DenmarkZ' or return a specific message:",countries.get("DenmarkZ","Not Found"))
print("- dict length:",len(countries))
