
import json
import matplotlib.pyplot as plt

def plot_graph(dataset):
    dataset_keys = list()
    dataset_values = list()
    for data in dataset:
        k = list(data.keys())[0]
        v = list(data.values())[0]
        dataset_keys.append(k)
        dataset_values.append(v)
    print("Keys:", dataset_keys)
    print("Values:", dataset_values)
    plt.plot(dataset_values)
    plt.ylabel('Requests per Date ')
    plt.xticks(range(len(dataset)), dataset_keys)
    plt.show()


def process_log():
    dataset = []
    with open("nginx.log", "r") as f:
        for line in f.readlines():
            line = line.strip('\n').split()
            ip = line[0]
            ts = line[3].split(':')
            date = ts[0].split('[')[1]
            item = [d for d in dataset if date in d]
            if len(item) == 0:
                dataset.append({date:1})
            else:
                d = item[0]
                idx = dataset.index(d)
                value = d[date] + 1
                dataset[idx] = {date:value}
                
    return dataset




plot_graph(process_log())
