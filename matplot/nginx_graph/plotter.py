
import json
import matplotlib.pyplot as plt

def plot_graph(dataset):
    dataset_keys = list()
    dataset_values = list()
    # for each dict, get its key
    for data in dataset:
        # obtaining day only from key (date)
        k = list(data.keys())[0].split('/')[0]
        v = list(data.values())[0]
        dataset_keys.append(k)
        dataset_values.append(v)
    plt.rcParams["figure.figsize"] = [12.4, 4.8]
    plt.plot(dataset_values)
    plt.ylabel('Requests per Date (September)')
    plt.xticks(range(len(dataset)), dataset_keys)
    plt.show()


def process_log():
    dataset = []
    with open("nginx.log", "r") as f:
        for line in f.readlines():
            line = line.strip('\n').split()
            # obtaining date only
            ts = line[3].split(':')
            date = ts[0].split('[')[1]
            # searching for date on dataset
            item = [d for d in dataset if date in d]
            # if date is not present on dataset: adding dict {date:1}
            if len(item) == 0:
                dataset.append({date:1})
            # else: date value will be incremented
            else:
                d = item[0]
                idx = dataset.index(d)
                value = d[date] + 1
                dataset[idx] = {date:value}

    return dataset




plot_graph(process_log())
