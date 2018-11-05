""" Find the numbers which are greater than 5.0, from a fixed data set. """

ds = {9.80, 2.7129, 50.2, 3.201, 1.620, 14.021, 19.32, 4.24, 8.99, 6.81, 6.3}

result = filter(lambda x: x > 5.0, ds)

print("\nData Set:\n", ds)
print("\nEven Numbers:\n", list(result))
