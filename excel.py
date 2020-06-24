import pandas
from read_h5 import *



data = pandas.read_csv('fichpris_v3.csv')
Liste_X = [0 for _ in range(450)]

for ind,el in enumerate(data.XP):
    if ind < 450:
        Liste_X[ind] = el
print(Liste_X[5])
