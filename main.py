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

connexion = sqlite3.connect("database.db")
curseur= connexion.cursor()
curseur.execute("PRAGMA foreign_keys = ON")



def main():
    print("how many variables do you wish to plot ? (the input) ")
    nb_variables = int(input())
    entry = []
    print("write down the variables")
    for _ in range(nb_variables):
        variable = input()
        entry.append(variable)
    print("what is the output?")
    output = input()



    ##units
    units = []
    begin_string = "SELECT "
    end_string = " FROM units "
    for data in entry:
        if data.startswith("KP_PS"):
            string = begin_string + "KPS" + end_string
        else:
            string = begin_string + data + end_string
        curseur.execute(string)
        unités = curseur.fetchall()
        units.append(unités[0][0])
    ##ouptu now
    if output.startswith("KP_PS"):
        string = begin_string + "KPS" + end_string
    else:
        string = begin_string + output + end_string
    curseur.execute(string)
    unités = curseur.fetchall()
    units.append(unités[0][0])



    print("How many conditions?")
    nb_conditions = int(input())
    print("Which one ?  ( ex : M0C < 0.25)")
    Conditions = []
    for _ in range(nb_conditions):
        cond = input()
        Conditions.append(cond)
    variable = ""
    end_string = " FROM données "

    for i in range(len(entry)):
        variable += entry[i]+ ", "
    variable += output + " "
    string = begin_string + variable + end_string
    if nb_conditions > 0:
        string += " WHERE "
        for indice in range(len(Conditions)):
            string = string + Conditions[indice]
            if indice != len(Conditions)-1:
                 string+=" AND "
    print(string)
    curseur.execute(string)
    variable_non_corrigée = [el for el in curseur.fetchall()]
    variable = []
    for el in (variable_non_corrigée):
        x=0
        for i in range(len(el)):
            if el[i] == 9999:
                x+=1
        if x ==0:
            variable.append(el)
    for el in variable:
        for i in range(len(el)):
            if el[i] == 9999:
                print(el)
    Liste = [[] for _ in range(nb_variables+1)]
    for i in range(nb_variables+1):
        Liste[i] = [x[i] for x in variable]
    if nb_variables == 1:
        plt.scatter(Liste[0], Liste[1])
        plt.xlabel(entry[0]+ " (" + units[0] + ")")
        plt.ylabel(output+ " (" + units[1] + ")")
        plt.show()
    elif nb_variables ==2:
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        ax.scatter(Liste[0], Liste[1],Liste[2])
        ax.set_xlabel(entry[0]+ " ("+  units[0]+ ")")
        ax.set_ylabel(entry[1]+ " (" + units[1] + ")")
        ax.set_zlabel(output+ " ("+units[2] + ")")
        plt.show()
    elif nb_variables == 3:
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        img = ax.scatter(Liste[0],Liste[1], Liste[2], c=Liste[3], cmap=plt.hot())
        ax.set_xlabel(entry[0] + " ("+ units[0] + ")")
        ax.set_ylabel(entry[1] + " ("+ units[1] + ")")
        ax.set_zlabel(entry[2] + " (" +units[2] + " )")
        plt.legend([output + " (" +units[3] + ")"])
        fig.colorbar(img)
        plt.show()







main()
