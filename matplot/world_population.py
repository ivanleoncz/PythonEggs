import matplotlib.pyplot as plt

print("\nWorld Population Graphic\n")

# axis
#
# year: horizontal
years = [1950, 1970, 1990, 2010]
# population: vertical
population = [2.519, 3.692, 5.263, 6.972]

# building graphic, depending on user input
opt = input("Lines or Scatter (l/s)? ")
if opt == "l":
    plt.plot(years, population)
elif opt == "s":
    plt.scatter(years, population)
else:
    print("Wrong option!")

# show graphic
plt.show()
