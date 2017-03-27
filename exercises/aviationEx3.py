import pandas as pd
import os
from urllib.parse import urlparse
import matplotlib.pyplot as plt
import heapq



def csv_to_df():
    return pd.read_csv('Aviation.csv', quotechar='"', skipinitialspace=True, delimiter=',',
                           encoding='latin1').fillna(0)

def ex3_dict_injury(dataframe):
    aircrafts = {}
    for row in dataframe.iterrows():
        temp = 0
        if pd.notnull(  row[1][23]  ):
            temp += row[1][23]
        if pd.notnull(  row[1][24]  ):
            temp += row[1][24]
        if pd.notnull(  row[1][25]  ):
            temp += row[1][25]

        if row[1][15] in aircrafts:
            aircrafts[row[1][15]] = temp
        else:
            aircrafts.setdefault(row[1][15], temp)

    return aircrafts

def top(d, n=None):
    li = heapq.nlargest(n, d, key=d.get)
    di = {}
    for ac in li:
        di[ac] = d.get(ac)
    return di

def dict_keys(d):
    return list(d.keys())

def dict_values(d):
    return list(d.values())

def plot(t5_k, t5_v):
    colors = ['Gold', 'Green', 'silver', 'blue', 'red']
    explode = (0.1, 0.0, 0.0, 0.0, 0.0) #explode first slice
    plt.pie(t5_v, explode=explode, labels=t5_k, colors=colors,
            autopct='%1.1f%%', shadow=True, startangle=90)

    plt.axis('equal')
    plt.title("...")
    plt.savefig('Question3Plot.png')
    plt.show()



url = 'https://github.com/edipetres/Depressed_Year/raw/master/Dataset_Assignment/AviationDataset.csv'
dataframe = csv_to_df()
aircrafts_dict = ex3_dict_injury(dataframe)
top_5 = top(aircrafts_dict, 5)
t5_k = dict_keys(top_5)
t5_v = dict_values(top_5)
plot(t5_k, t5_v)




