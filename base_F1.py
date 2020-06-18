#! python3
import matplotlib.pyplot as plt
from convert_h5_bon_format import *



import sqlite3
sqlite3.register_adapter(numpy.int32, lambda val: int(val))
sqlite3.register_adapter(numpy.float32, lambda val: float(val))
sqlite3.register_adapter(numpy.int64, lambda val: int(val))
sqlite3.register_adapter(numpy.float64, lambda val: float(val))

# connexion= sqlite3.connect("premiere_tentative.db")
connexion = sqlite3.connect(":memory:")
curseur= connexion.cursor()
curseur.execute("PRAGMA foreign_keys = ON")
##on cree la base de donnee
create_table(connexion, table_force_pression_essaie)

donnees_essaie= [("F1","04/19", "LRM-F1 M378.5.14002", "Rear sting on quadrant holder", "Onera"),("F1","09/19", "LRM-F1 M378.5.14002", "Monostrut", "Onera") ]
curseur.executemany("INSERT INTO essaie (soufflerie, date, Model, Model_setup, organisation) VALUES (?, ?,?,?,?)",donnees_essaie)




##On met d abord les fichiers forces (h5 TOUT)
liste_numero = [550,551,552,553,554,555,558,559,626,627]
x = 1
for nb in liste_numero:
    fichier_h5 = "F1-2019_09_DT_Reception_LRMF1_1M_29094-008F-small\Donnée\{}_TOUT.H5".format(nb)
    print(nb)
    put_file_in_bdd(fichier_h5,x, curseur)
    # if nb%3 ==0:
    #     for ligne in curseur.execute("SELECT * FROM données_force"):
    #         print("données :", ligne)
    #         print("\n")



# curseur.execute("SELECT ALPHAC,CXC FROM données_force WHERE RE0C >3000000 ")
# Tuple_alpha_cxc = [(el[0], el[1]) for el in curseur.fetchall()]
# Tuple_alpha_cxc.sort(key=lambda tup: tup[0])
# alpha = [alph[0] for alph in Tuple_alpha_cxc]
# cxc = [cxc[1] for cxc in Tuple_alpha_cxc]
# plt.plot(alpha, cxc)
# plt.xlabel('alpha')
# plt.ylabel('cxc')
# plt.show()
#











connexion.commit()

connexion.close()
