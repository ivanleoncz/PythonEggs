import pandas as pd

countries = ['China', 'India', 'USA', 'Indonesia', 'Brazil']

ds = pd.Series(countries)

# changing interval for RangeIndex object
ds.index += 1

print(ds)
