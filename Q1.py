import numpy as np, matplotlib.pyplot as plt, pandas as pd,collections, sys, csv, urllib.request
from collections import OrderedDict
from operator import itemgetter
database = pd.read_csv('Aviation.csv',quotechar='"',skipinitialspace=True, delimiter=',', encoding='latin1').fillna(0)
data = database.as_matrix()

d = collections.defaultdict(list)

for row in data:
    key = row[28]
    if key == "" or key == 0: continue
    val = 0 if(row[23]) ==""  else float(row[23])
    d.setdefault(key,[]).append(val)

d2 = {}
for k, v in d.items(): d2[k] = sum(v)
for k, v in d2.items(): print ("{}:{}".format(k,v))

# OrderedDict to get dict sorted
sortedd2 = OrderedDict(sorted(d2.items(), key=itemgetter(1)))


# Ploting
y_pos = np.arange(len(d2))
for a,b in zip(y_pos, sortedd2.values()):
	plt.text(a-0.25, b+10, str("%.0f" % b))
plt.bar(y_pos, sortedd2.values(), align='center', alpha=0.5)
plt.xticks(y_pos, sortedd2.keys(), rotation=90)
plt.ylabel('Amount of fatalities')
plt.title('How do the flight phases contribute to fatalities?')
plt.savefig('Question1.png', bbox_inches='tight')

# database.groupby('Broad.Phase.of.Flight')['Total.Fatal.Injuries'].sum().plot.bar()

