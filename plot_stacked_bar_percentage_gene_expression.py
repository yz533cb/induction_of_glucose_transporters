import platereader as pr
import matplotlib.pyplot as plt
import pandas as pd
import pickle

p, a1, a2, b1, b2, c1, c2, d1, d2, e1, e2, f1, f2 = pickle.load(open('day1.pkl', 'rb'))
P, t = p.d, p.t

# Make data chart

Day11 = [P['Glu 1%']['Hxt2']['mg'],
        P['Glu 1%']['Hxt3']['mg'],
        P['Glu 1%']['Hxt4']['mg'],
        P['Glu 1%']['Hxt7']['mg'],
        P['Glu 1%']['Gal2']['mg']]

dataframe = pd.DataFrame(Day11, columns = t)
dataframe = dataframe.transpose()
dataframe.columns = ['Hxt2', 'Hxt3', 'Hxt4', 'Hxt7', 'Gal2']

# Calculate each GFP in percentage

totals = [ i + j + k + l + m for i, j, k, l, m in zip(dataframe['Hxt2'], dataframe['Hxt3'], dataframe['Hxt4'], dataframe['Hxt7'], dataframe['Gal2'])]

Hxt2_rel = [ i/j*100 for i, j in zip(dataframe['Hxt2'], totals)]
Hxt3_rel = [ i/j*100 for i, j in zip(dataframe['Hxt3'], totals)]
Hxt4_rel = [ i/j*100 for i, j in zip(dataframe['Hxt4'], totals)]
Hxt7_rel = [ i/j*100 for i, j in zip(dataframe['Hxt7'], totals)]
Gal2_rel = [ i/j*100 for i, j in zip(dataframe['Gal2'], totals)]

# Stacked bar figure
       
f, ax = plt.subplots(1, figsize = (7, 7))

bar_width = 0.19
bar_length = t

ax.bar(bar_length, Hxt2_rel, label = 'Hxt2', alpha = 0.7, color = 'red', width = bar_width)
ax.bar(bar_length, Hxt3_rel, bottom = Hxt2_rel, label = 'Hxt3', alpha = 0.7, color = 'blue', width = bar_width)
ax.bar(bar_length, Hxt4_rel, bottom = [i + j for i, j in zip(Hxt2_rel, Hxt3_rel)], label = 'Hxt4', alpha = 0.7, color = 'green', width = bar_width)
ax.bar(bar_length, Hxt7_rel, bottom = [i + j + k for i, j, k in zip(Hxt2_rel, Hxt3_rel, Hxt4_rel)], label = 'Hxt7', alpha = 0.7, color = 'silver', width = bar_width)
ax.bar(bar_length, Gal2_rel, bottom = [i + j + k + l for i, j, k, l in zip(Hxt2_rel, Hxt3_rel, Hxt4_rel, Hxt7_rel)], label = 'Gal2', alpha = 0.7, color = 'yellow', width = bar_width)

plt.xlim(0, 20)
plt.xlabel('Time (hours)')
plt.ylim(0, 100)
plt.ylabel('GFP (%) per cell')
plt.title('GFP Percentage per Cell of Hxt2/3/4/7 Gal2 in 1% Glucose from Day 1')
plt.legend(loc=1)
plt.show()
