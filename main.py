from os import stat
import plotly.figure_factory as ff
import plotly.graph_objects as go
import statistics
import random
import csv
import pandas as pd

df = pd.read_csv('medium_data.csv')
data = df['reading_time'].tolist()
population_mean = statistics.mean(data)
std_deviation = statistics.stdev(data)


dataset = []
for i in range(0,100):
    random_index = random.randint(0,len(data))
    value = data[random_index]
    dataset.append(value)
mean = statistics.mean(dataset)
std_deviation_of_sample = statistics.stdev(dataset)
print("Population mean is - ", population_mean)
print("Standard Deviation is - ", std_deviation)
print("Sample mean is - ", mean)
print("Sample standard Deviation is - ", std_deviation_of_sample)

def random_set_of_mean(counter):
    dataset = []
    for i in range(0, counter):
        random_index = random.randint(0, len(data)-1)
        value = data[random_index]
        dataset.append(value)
    mean = statistics.mean(dataset)
    return mean

def show_fig(mean_list):
    df = mean_list
    mean = statistics.mean(df)
    fig = ff.create_distplot([df], ["reading_time"], show_hist=False)
    fig.add_trace(go.Scatter(x=[mean, mean], y=[0, 1], mode = "lines", name = "Mean"))
    fig.show()

def setup():
    mean_list = []
    for i in range(0, 1000):
        set_of_means = random_set_of_mean(100)
        mean_list.append(set_of_means)
    show_fig(mean_list)
    mean = statistics.mean(mean_list)
    print("Mean of sampling distribution :-", mean)
setup()

