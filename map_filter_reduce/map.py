""" Calculate the quartile of each numbers from a fixed data set.
"""

data_set = [30.9080, 234.7800012, 203.8901, 189.6240, 14.60021, 119.032, 44.04]

r = map(lambda x: x / 4, data_set)

print("\nData Set:\n", data_set)
print("\nQuartile of each value:\n", list(r))
