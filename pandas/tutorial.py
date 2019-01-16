import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# COUNTRIES as indexes.
#
countries = ["Brazil", "Germany", "Egypt", "China", "Uruguay", "Sudan", "Congo"]
s = pd.Series(countries)
print("\nSeries:\n",s)

# DATES as indexes.
#
#dates = pd.date_range('20171101', periods=30)
#print("\n", dates)

years = ['2015', '2016', '2017', '2018']
letters = ['A', 'B', 'C', 'D']

# index attribute is flexible, 
df = pd.DataFrame(np.random.randn(7, 4), index=countries, columns=years)
print("\n\nDataFrame - all data:\n", df)
print("\n\nDataFrame - head (2) of data:\n", df.head(2))
print("\n\nDataFrame - tail (4) of data:\n", df.tail(4))
print("\n\nDataFrame - index:\n", df.index)
print("\n\nDataFrame - columns:\n", df.columns)
print("\n\nDataFrame - values:\n", df.values)
