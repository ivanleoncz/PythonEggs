#!/usr/bin/python3

import pandas as pd
import numpy as np

print("\nFrom ndarray:")
data = np.array(['a','b','c','d'])
s = pd.Series(data)
print(s)

print("\nFrom ndarray (index starting in 100):")
data = np.array(['a','b','c','d'])
s = pd.Series(data, index=[100, 101, 102, 103])
print(s)

print("\nFrom dict:")
data = {"2xx":4623, "3xx":230, "4xx": 82, "5xx":21}
s = pd.Series(data)
print(s)
