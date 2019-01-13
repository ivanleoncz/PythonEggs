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
print(df)

