import platereader as pr
import fitOD as f

# GFP data analyze process with media and WT

p = pr.platereader('*data.xlsx', '*contents.xls')   * is the save file name, can be date etc.
p.plotraw('od')

p.mediacorrect(figs = True)
p.plotraw('od')

p.processWT(noruns = 5, figs = True)
p.correctfef(5)
p.plotcorrected()

# Fit OD

P, t = p.d, p.t

a1 = f.fitOD(t, P['Glu 1%']['WT']['data'][:, ::3], noruns = 10, figs = True)
a2 = f.fitOD(t, P['Glu 2%']['WT']['data'][:, ::3], noruns = 10, figs = True)

# Save data

import pickle

pickle.dump((p, a1, a2), open('*.pkl', 'wb'))
