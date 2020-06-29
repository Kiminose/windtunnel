#! python3
import matplotlib.pyplot as plt
from convert_h5_bon_format import *

from pathlib import Path

import sqlite3
sqlite3.register_adapter(numpy.int32, lambda val: int(val))
sqlite3.register_adapter(numpy.float32, lambda val: float(val))
sqlite3.register_adapter(numpy.int64, lambda val: int(val))
sqlite3.register_adapter(numpy.float64, lambda val: float(val))

connexion= sqlite3.connect("database.db")
curseur= connexion.cursor()
curseur.execute("PRAGMA foreign_keys = ON")

#On met d abord les fichiers forces (h5 TOUT)
i =0
pathlist = Path(r'F1-2019_09_DT_Reception_LRMF1_1M_29094-008F').glob('**/*.H5')
x=0
for file in pathlist:
     # because path is object not string
    fichier_h5 = str(file)
    name = str(fichier_h5)

    if "PPK" in fichier_h5:
        if name[-12].isdigit():
            numero = int(name[-12:-8])
        else:
            numero = int(name[-11:-8])
        fichier_h5_pressure = file
        fichier_h5_force = r'F1-2019_09_DT_Reception_LRMF1_1M_29094-008F/{}_TOUT.H5'.format(numero)
        put_file_in_bdd(fichier_h5_force,fichier_h5_pressure, curseur)
        print(i)
        i = i+1


connexion.commit()

connexion.close()
