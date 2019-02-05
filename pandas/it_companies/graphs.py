import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("it_companies.csv", header=None)

print("\nBefore:")
print(df)

new_index = list(df[0])
new_columns = [2013, 2014, 2015, 2016, 2017, 2018]
del df[0]
df.columns = new_columns
df.index = new_index

print("\nAfter:")
print(df)

df.to_csv("it_companies_new.csv", header=None)

plt.plot(df.columns, df.iloc[0], label="IBM")
plt.plot(df.columns, df.iloc[1], label="Microsoft")
plt.plot(df.columns, df.iloc[2], label="Apple")
plt.plot(df.columns, df.iloc[3], label="HP")


plt.locator_params(axis="y")
plt.locator_params(axis="x", nbins=len(df.columns))
plt.ylim(0, 10)
plt.xlabel("Years")
plt.ylabel("GDP in U$ (Bi)")
plt.title("GDP x Years")
plt.legend()
plt.savefig('plot.png')

plt.show()
