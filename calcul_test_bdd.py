#! python3

import sqlite3
import numpy
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from read_h5 import *



sqlite3.register_adapter(numpy.int32, lambda val: int(val))
sqlite3.register_adapter(numpy.float32, lambda val: float(val))
sqlite3.register_adapter(numpy.int64, lambda val: int(val))
sqlite3.register_adapter(numpy.float64, lambda val: float(val))

# connexion= sqlite3.connect("premiere_tentative.db")
connexion = sqlite3.connect("database.db")
curseur= connexion.cursor()
curseur.execute("PRAGMA foreign_keys = ON")


# curseur.execute("SELECT * FROM données WHERE NLOT = 550 AND ALPHAC = 20.37739372253418")
# P1 = [ el for indi,el in enumerate(curseur.fetchall()[0]) if indi > 18]
#
#
# curseur.execute("SELECT * FROM position_captor_X")
# L1 = [x for x in curseur.fetchall()[0]]
# L1.pop(0)
# curseur.execute("SELECT * FROM position_captor_Y")
# L2 = [x for x in curseur.fetchall()[0]]
# L2.pop(0)
# curseur.execute("SELECT * FROM position_captor_Z")
# L3 = [x for x in curseur.fetchall()[0]]
# L3.pop(0)
#
# X = []
# Y = []
# Z = []
# pressure = []
#
# for x,y,z,pres in zip(L1,L2,L3,P1):
#     if pres != 9999:
#         X.append(x)
#         Y.append(y)
#         Z.append(z)
#         pressure.append(-pres)
#
#
# fig = plt.figure()
# ax = fig.add_subplot(111, projection='3d')
#
#
# img = ax.scatter(X, Y, Z, c=pressure, cmap=plt.gray())
# fig.colorbar(img)
#
# plt.show()
# fig = plt.figure()
# ax = fig.gca(projection='3d')
# ax.scatter(X, Y, Z, label='parametric curve')
# ax.legend()



curseur.execute("SELECT ALPHAC, BETA, RE0C FROM données ")

# Alpha_prec = [(el[0], el[1]) for el in curseur.fetchall()]
#
# Alpha_prec.sort(key=lambda tup: tup[0])
#
Tuple_alpha_cxc = [(el[0], el[1], el[2]) for el in curseur.fetchall()]
#Tuple_alpha_cxc.sort(key=lambda tup: tup[0])
alpha = [alph[0] for alph in Tuple_alpha_cxc]
beta = [cxc[1] for cxc in Tuple_alpha_cxc]
Moc = [cxc[2] for cxc in Tuple_alpha_cxc]

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
#
#
ax.scatter(alpha, beta, Moc)
plt.xlabel('alpha')
plt.ylabel('beta')
plt.legend(["M0C"])
plt.show()

#

# alpha = [alph[0] for alph in Alpha_prec]
# moc =  [alph[1] for alph in Alpha_prec]
# cxc = [cxc[2] for cxc in Alpha_prec]

#
