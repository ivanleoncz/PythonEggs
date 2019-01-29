import pandas as pd

d = {
        'Name':['IBM', 'Microsoft', 'Apple', 'HP'],
        'Growth (%)':[3.6, 2.8, 2.9, 2.4],
        'Growth (Mi U$)':[39, 43, 41, 27]
}

years = [2018, 2017, 2016, 2015]

df = pd.DataFrame(d, index = years)

print(df)
