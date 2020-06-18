#! python3

import sqlite3
import numpy
import matplotlib.pyplot as plt


sqlite3.register_adapter(numpy.int32, lambda val: int(val))
sqlite3.register_adapter(numpy.float32, lambda val: float(val))
sqlite3.register_adapter(numpy.int64, lambda val: int(val))
sqlite3.register_adapter(numpy.float64, lambda val: float(val))

# connexion= sqlite3.connect("premiere_tentative.db")
connexion = sqlite3.connect("premiere_tentative")
curseur= connexion.cursor()
curseur.execute("PRAGMA foreign_keys = ON")
##on cree la base de donnee



curseur.execute("SELECT ALPHAC,NPT FROM données_force WHERE NLOT = 550")
Tuple_alpha = [(el[0], el[1]) for el in curseur.fetchall()]
curseur.execute("SELECT KP_PS3204,NPT FROM données_pressure WHERE NLOT = 550")
Tuple_KP_PS3204 = [(el[0], el[1]) for el in curseur.fetchall()]
Tuple_alpha.sort(key=lambda tup: tup[1])
Tuple_KP_PS3204.sort(key=lambda tup: tup[1])
Tuple_alpha_pressure = [(el1[0], el2[0]) for (el1,el2) in zip(Tuple_alpha,Tuple_KP_PS3204)]
alpha = [alph[0] for alph in Tuple_alpha_pressure]
pressure = [cxc[1] for cxc in Tuple_alpha_pressure]
# Tuple_alpha_cxc = [(el[0], el[1]) for el in curseur.fetchall()]
# Tuple_alpha_cxc.sort(key=lambda tup: tup[0])
# alpha = [alph[0] for alph in Tuple_alpha_cxc]
# cxc = [cxc[1] for cxc in Tuple_alpha_cxc]
plt.plot(alpha, pressure)
plt.xlabel('alpha')
plt.ylabel('pressure')
plt.show()
