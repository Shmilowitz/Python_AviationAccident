import numpy as np, matplotlib.pyplot as plt, pandas as pd,collections, sys, csv, urllib.request
from collections import OrderedDict
import operator
df = pd.read_csv('AviationDataset.csv',quotechar='"',skipinitialspace=True, delimiter=',', encoding='latin1').fillna(0)
data = df.as_matrix()

dDeath = collections.defaultdict(list)


for row in data:
	if row[3] < '1997-01-01': continue
	key = row[3][0:4]
	val = 0 if(row[23]) ==""  else float(row[23])
	dDeath.setdefault(key,[]).append(val)
d2Death = {}
for k, v in dDeath.items(): d2Death[k] = sum(v)
for k, v in d2Death.items(): print ("{}:{} Deaths".format(k,v))


y_pos = np.arange(len(d2Death))
plt.bar(y_pos, d2Death.values())
plt.xticks(y_pos, d2Death.keys(), rotation=90)
plt.title('What was the distribution of fatal injuries during the last 20 years?')
plt.ylabel('Amount of fatal injuries')
for a,b in zip(y_pos, d2Death.values()):
	plt.text(a-0.25, 500, str("%.0f" % b), rotation=90, color = 'black')
plt.savefig('Question4.png', bbox_inches='tight')
plt.show()