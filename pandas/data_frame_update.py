#!/usr/bin/python3

import pandas as pd


# DataFrame with index starting at 1
cities = [
            ["Guaíba", "Rio Grande do Sul", "Brazil"],
            ["Xalapa", "Veracruz", "Mexico"],
            ["San Antonio", "Texas", "USA"],
            ["Campinas", "São Paulo", "Brazil"]
        ]

df = pd.DataFrame(cities, columns = ["City", "State", "Country"])
df.index += 1

print("Simple DataFrame:\n")
print(df)

print("\nUpdating Row Label 3 / Column Label 'City':\n")
df.at[4, "City"] = "Itupeva"
print(df)

print("\nUpdating Row Index 1 / Column Integer 0:\n")
df.iat[1, 0] = "Xalapa-Enríquez"
print(df)
