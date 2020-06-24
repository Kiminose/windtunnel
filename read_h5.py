#! python


##this file is used to read un .H5
##
import h5py
import numpy
import matplotlib.pyplot
import pandas
import datetime






def read_h5(filename):
##convert a .H5 into a dataframzn easy to manipulate
    def selectValues(name, obj):
        if 'VALUES' in name:
            lstDataSets.append(obj)
    lstDataSets = []
    with h5py.File(filename, mode='r') as of:
        of.visititems(selectValues)
        lstDataFrames = [pandas.DataFrame(dset[:,0]) for dset in lstDataSets]
        data = pandas.concat(lstDataFrames)
        data.rename(columns={col:col.strip(' ').upper() for col in data.columns.tolist()}, inplace=True)
        if "DATETIME" in data.columns:
            data["DATETIME"] = pandas.to_datetime(data["DATETIME"].str.decode("utf-8"))
            data.set_index("DATETIME", inplace=True)
        # elif "NPT" in data.columns:
        #     data.set_index("NPT", inplace=True)
        data.sort_index(inplace=True)
        data.replace(9999., numpy.nan)
    return data




def convert_h5force_dataframe(fichier):
##ONLY USED FOR FILE ; ***_TOUT.H5
##select the data chosed in the Note provisoire à finaliser à l’issue du stage de F. Pourré version 0.1, Date : 15 juin 2020
    Données_recueilles_force = ["NROT", "NLOT", "M0C", "RE0C", "PI0", "TI",
        "ALPHAC", "BETA", "CXC", "CYC", "CZC", "CLAAC" , "CMAAC", "CNAAC", "Wing", "HTP", "VTP", "DATETIME", "NPT"]

    for element in fichier.columns:
        if element not in Données_recueilles_force:
            ##we delete the useless columns
            del fichier[element]
##we decode and turn the ('avec, sans') into (1/0)
    for element in fichier.columns:
        if type(fichier[element][0]) == bytes:
            for i in range(len(fichier[element])):
                fichier[element][i] = fichier[element][i].decode()
                if fichier[element][i] == "AVEC":
                    fichier[element][i] = 1
                else:
                    fichier[element][i] =0


def convert_h5pressure_dataframe(fichier):
    ##ONLY USED for file PPK_.H5
    ##we only keep Pressure coefficient
    for element in fichier.columns:
        if not (element.startswith("KP_PS")) :
            del fichier[element]





def code_confog_maquette(fichier):
    ##we add the configuration of the plane according to the pdf Note provisoire à finaliser à l’issue du stage de F. Pourré version 0.1, Date : 15 juin 2020
    fichier["CONF"] = ""
    for i in range(len(fichier["CONF"])):

        if fichier["HTP"][i] == 0 and fichier["VTP"][i] == 0:
            fichier["CONF"][i] = "BW"
        elif fichier["HTP"][i] == 1 and fichier["VTP"][i] == 0:
            fichier["CONF"][i] = "BWH"
        elif fichier["HTP"][i] == 1 and fichier["VTP"][i] == 1:
            fichier["CONF"][i] = "BWHV"
    del fichier["HTP"]
    del fichier["VTP"]
