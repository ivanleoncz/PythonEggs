#!/usr/bin/python3

fruits = [ {"Banana":4},{"Apple":8},{"Grape":5} ]

for d in fruits:
    print("\nDictionary: ", d)
    for key,value in d.items():
        print("Key: ",key)
        print("Value:",value)
        if key == "Apple":
            print("Found!")
            value += 1
            d[key] = value
            print("New Amount of Apples: ",d)
