""" Calculate the quartile of each numbers from a fixed data set.
"""

ds = {30.9080, 234.7800012, 203.8901, 189.6240, 14.60021, 119.032, 44.04}

result = map(lambda x: x / 4, ds)

print("\nData Set:\n", ds)
print("\nQuartile of each value:\n", list(result))
