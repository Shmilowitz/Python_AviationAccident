import numpy as np, matplotlib.pyplot as plt, pandas as pd,collections, sys, csv, urllib.request
from collections import OrderedDict
import operator
df = pd.read_csv('Aviation.csv',quotechar='"',skipinitialspace=True, delimiter=',', encoding='latin1').fillna(0)
data = df.as_matrix()

dDeath = collections.defaultdict(list)
dSurv = collections.defaultdict(list)



for row in data:
	if row[3] < '1993-01-01': continue
	if row[11] == 'Destroyed' or row[11] == 'Substantial':
		key = row[3][0:4]
		val = 0 if(row[23]) ==""  else float(row[23])
		dDeath.setdefault(key,[]).append(val)
		val = 0 if(row[24] or row[25] or row[26]) ==""  else float(row[24]) + float(row[25]) + float(row[26])
		dSurv.setdefault(key,[]).append(val)
d2Death = {}
for k, v in dDeath.items(): d2Death[k] = sum(v)
for k, v in d2Death.items(): print ("{}:{} Deaths".format(k,v))

d2Surv = {}
for k, v in dSurv.items(): d2Surv[k] = sum(v)
for k, v in d2Surv.items(): print ("{}:{} Survs".format(k,v))


SurvValues = d2Surv.values()
DeathValues = d2Death.values()

y_pos = np.arange(len(d2Death))
p1 = plt.bar(y_pos, SurvValues, color = '#8080ff')
p2 = plt.bar(y_pos, DeathValues, color = 'r', bottom = SurvValues)
plt.xticks(y_pos, d2Surv.keys(), rotation=90)
plt.title('Survival rate')
plt.legend((p1[0], p2[0]), ('Survivers', 'Deaths'))
for a,b,c in zip(y_pos, SurvValues, DeathValues):
	plt.text(a-0.25, 650, str("%.0f" % (b / ((b+c) / 100))) + '%', rotation=90, color = 'black')
	plt.text(a-0.25, b+c+650, str("%.0f" % (c / ((b+c) / 100))) + '%', rotation=90)
plt.savefig('Question5.png', bbox_inches='tight')
plt.show()

# for row in data:
	# if row[3] < '1993-01-01': continue
	# if row[11] == 'Destroyed' or row[11] == 'Substantial':
		# key = row[3][0:4]
		# val = 0 if(row[24] or row[25] or row[26]) ==""  else float(row[24]) + float(row[25]) + float(row[26])
		# dSurv.setdefault(key,[]).append(val)
# print(d2)


