#! python3

import sqlite3
import numpy
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from read_h5 import *


data = read_h5(r'F1-2019_09_DT_Reception_LRMF1_1M_29094-008F/550_PPKP.H5')
print(data.columns)
# sqlite3.register_adapter(numpy.int32, lambda val: int(val))
# sqlite3.register_adapter(numpy.float32, lambda val: float(val))
# sqlite3.register_adapter(numpy.int64, lambda val: int(val))
# sqlite3.register_adapter(numpy.float64, lambda val: float(val))
#
# # connexion= sqlite3.connect("premiere_tentative.db")
# connexion = sqlite3.connect("database.db")
# curseur= connexion.cursor()
# curseur.execute("PRAGMA foreign_keys = ON")
# ##on cree la base de donnee
#
#
#
# curseur.execute("SELECT ALPHAC,BETA, CXC FROM données WHERE NLOT = 550 ")
# Alpha_prec = [(el[0], el[1], el[2]) for el in curseur.fetchall()]
#
# Alpha_prec.sort(key=lambda tup: tup[0])
#
# # Tuple_alpha_cxc = [(el[0], el[1]) for el in curseur.fetchall()]
# # Tuple_alpha_cxc.sort(key=lambda tup: tup[0])
# # alpha = [alph[0] for alph in Tuple_alpha_cxc]
# # cxc = [cxc[1] for cxc in Tuple_alpha_cxc]
# # plt.plot(alpha, pressure)
# # plt.xlabel('alpha')
# # plt.ylabel('pressure')
# # plt.show()
#
#
# fig = plt.figure()
# ax = fig.gca(projection='3d')
# alpha = [alph[0] for alph in Alpha_prec]
# moc =  [alph[1] for alph in Alpha_prec]
# cxc = [cxc[2] for cxc in Alpha_prec]
# ax.plot(alpha, moc, cxc, label='parametric curve')
# ax.legend()
#
# plt.show()
