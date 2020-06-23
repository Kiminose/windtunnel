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



curseur.execute("SELECT ALPHAC,NPT, NLOT FROM données_force WHERE M0C < 0.2")
Tuple_alpha = [(el[0], el[1], el[2]) for el in curseur.fetchall()]
curseur.execute("SELECT KP_PS3204,NPT,NLOT FROM données_pressure")
Tuple_KP_PS3204 = [(el[0], el[1], el[2]) for el in curseur.fetchall()]
Alpha_prec = [(0,0) for _ in range(len(Tuple_alpha))]
i =0


Alpha_prec.sort(key=lambda tup: tup[0])
alpha = [alph[0] for alph in Alpha_prec]
pressure = [cxc[1] for cxc in Alpha_prec]
# Tuple_alpha_cxc = [(el[0], el[1]) for el in curseur.fetchall()]
# Tuple_alpha_cxc.sort(key=lambda tup: tup[0])
# alpha = [alph[0] for alph in Tuple_alpha_cxc]
# cxc = [cxc[1] for cxc in Tuple_alpha_cxc]
plt.plot(alpha, pressure)
plt.xlabel('alpha')
plt.ylabel('pressure')
plt.show()
