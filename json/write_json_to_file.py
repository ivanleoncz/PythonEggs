import json

filename = "user_data"

d = {"username":"ivanleoncz", "role":"Software Developer"}

with open('{}.json'.format(filename), 'w') as out:
    json.dump(d, out)
