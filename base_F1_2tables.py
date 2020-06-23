#! python3
import matplotlib.pyplot as plt
from convert_h5_bon_format import *

from pathlib import Path

import sqlite3
sqlite3.register_adapter(numpy.int32, lambda val: int(val))
sqlite3.register_adapter(numpy.float32, lambda val: float(val))
sqlite3.register_adapter(numpy.int64, lambda val: int(val))
sqlite3.register_adapter(numpy.float64, lambda val: float(val))

# connexion= sqlite3.connect("premiere_tentative.db")
connexion = sqlite3.connect("premiere_tentative")
curseur= connexion.cursor()
curseur.execute("PRAGMA foreign_keys = ON")
##on cree la base de donnee
create_table(connexion, table_force_pression_essaie)

donnees_essaie= [("F1","04/19", "LRM-F1 M378.5.14002", "Rear sting on quadrant holder", "Onera"),("F1","09/19", "LRM-F1 M378.5.14002", "Monostrut", "Onera") ]
curseur.executemany("INSERT INTO essaie (soufflerie, date, Model, Model_setup, organisation) VALUES (?, ?,?,?,?)",donnees_essaie)






#On met d abord les fichiers forces (h5 TOUT)
i =0
pathlist = Path(r'F1-2019_09_DT_Reception_LRMF1_1M_29094-008F').glob('**/*.H5')
for file in pathlist:
     # because path is object not string
    fichier_h5 = str(file)
    if "PPK" in fichier_h5:
        x=0
    else:
        x = 1
    put_file_in_bdd(fichier_h5,x, curseur)
    if i%20 == 0:
        print(i)
    i = i+1






connexion.commit()

connexion.close()
