import numpy as np, matplotlib.pyplot as plt, pandas as pd,collections, sys, csv, urllib.request
from collections import OrderedDict
import operator
database = pd.read_csv('Aviation.csv',quotechar='"',skipinitialspace=True, delimiter=',', encoding='latin1').fillna(0)
data = database.as_matrix()

d = collections.defaultdict(list)
maskUS =  (data[:,5] == 'United States')
print(data[:,3])