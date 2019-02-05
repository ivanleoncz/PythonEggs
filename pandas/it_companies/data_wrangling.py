import pandas as pd

df = pd.read_csv("it_companies.csv", header=None)

print("\nBefore:")
print(df)

new_index = list(df[0])
new_columns = [2016, 2017, 2018]
del df[0]
df.columns = new_columns
df.index = new_index

print("\nAfter:")
print(df)
