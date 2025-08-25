import platereader as pr
import matplotlib.pyplot as plt

import pickle

p, a1, a2 = pickle.load(open('*.pkl', 'rb'))

P, t = p.d, p.t

# GFP with error bars

plt.figure()

plt.plot(t, P['Glu 1%']['WT']['mg'], color = 'b', label = '1% glicose')
plt.errorbar(t, P['Glu 1%']['WT']['mg'], yerr= P['Glu 1%']['WT']['sg'], ecolor='k', alpha=0.2)

plt.plot(t, P['Glu 2%']['WT']['mg'], color = 'r', label = '2% glicose')
plt.errorbar(t, P['Glu 2%']['WT']['mg'], yerr= P['Glu 2%']['WT']['sg'], ecolor='k', alpha=0.2)

plt.xlim(0, 20)
plt.ylim(0, 2500)
plt.show()
