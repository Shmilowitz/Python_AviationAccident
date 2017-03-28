import numpy as np, matplotlib.pyplot as plt, pandas as pd,collections, sys, csv, urllib.request
from collections import OrderedDict
import operator
database = pd.read_csv('AviationDataset.csv',quotechar='"',skipinitialspace=True, delimiter=',', encoding='latin1').fillna(0)
data = database.as_matrix()

d = collections.defaultdict(list)
maskUS =  (data[:,5] == 'United States')
for row in data[maskUS]:
    key = row[4]
    if key == "" or key == 0: continue
    val = 0 if(row[24]) =="" else float(row[24]+row[25])
    d.setdefault(key,[]).append(val)

d2 = {}
for k, v in d.items(): d2[k] = sum(v)
# for k, v in d2.items(): print ("{}:{}".format(k,v))

#Top5 dict
top5 = dict(sorted(d2.items(), key=operator.itemgetter(1), reverse=True)[:5])
print(top5)

y_pos = np.arange(len(top5))
for a,b in zip(y_pos, top5.values()):
	plt.text(a-0.25, b+2, str(b))
plt.bar(y_pos, top5.values(), align='center', alpha=0.5)
plt.xticks(y_pos, top5.keys(), rotation=90)
plt.ylabel('Injuries per state')
plt.title('Which 5 states saw the most injuries in the US?')
plt.savefig('Question2.png', bbox_inches='tight')