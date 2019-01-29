import matplotlib.pyplot as plt

print("\nWorld Population Graphic\n")

# axis
#
# year: horizontal
years = [1950, 1960, 1970, 1980, 1990, 2000, 2010]
# population: vertical
population = [2.584, 3.033, 3.700, 4.458, 5.331, 6.145, 6.958]

# building graphic, depending on user input
opt = input("Lines / Scatter / Histogram (l/s/h)? ")
if opt == "l":
    plt.plot(years, population)
    plt.grid(True)
elif opt == "s":
    plt.scatter(years, population)
    plt.grid(True)
elif opt == "h":
    plt.hist(population, bins=5)
else:
    print("Wrong option!")

# show graphic
plt.show()
