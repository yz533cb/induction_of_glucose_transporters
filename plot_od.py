import platereader as pr
import matplotlib.pyplot as plt
import numpy as np

# Load data

import pickle
p, a1, a2 = pickle.load(open('*.pkl', 'rb'))
t = p.t

# OD of strains in different sugar concentrations

plt.figure()

plt.plot(t, a1.fod, 'b', label = '1% glucose')
plt.fill_between(t, a1.fod-np.sqrt(a1.fodvar), a1.fod+np.sqrt(a1.fodvar), facecolor='blue', alpha=0.2)
plt.plot(t, a2.fod, 'r', label = '2% glucose')
plt.fill_between(t, a2.fod-np.sqrt(a2.fodvar), a2.fod+np.sqrt(a2.fodvar), facecolor='red', alpha=0.2)

plt.xlim(0, 20)
plt.ylim(-1.5, 0.5)
plt.ylabel('Log OD')
plt.title('OD with error bars')
plt.show()
