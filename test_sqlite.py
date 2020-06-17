#! python3


import sqlite3
connexion= sqlite3.connect("basedonnee.db")
curseur= connexion.cursor()
curseur.execute("PRAGMA foreign_keys = ON")
curseur.executescript("""
    CREATE TABLE IF NOT EXISTS joueurs(id_joueur INTEGER PRIMARY KEY,
    pseudo TEXT,mdp TEXT);
    CREATE TABLE IF NOT EXISTS scores(
    id_score INTEGER PRIMARY KEY,
    fk_joueur INTEGER NOT NULL,
    valeur INTEGER,
    FOREIGN KEY(fk_joueur) REFERENCES joueurs(id_joueur)
    ON DELETE CASCADE);
    DELETE FROM joueurs;""")
donnees_joueur= [("toto","123"),("tata","azerty"),("titi","qwerty") ]
donnees_score= [(1,1000),(2,750),(3,500) ]
curseur.executemany("INSERT INTO joueurs (pseudo, mdp) VALUES (?, ?)",donnees_joueur)
curseur.executemany("INSERT INTO scores (fk_joueur, valeur) VALUES (?, ?)",donnees_score)
connexion.commit()
for joueur in curseur.execute("SELECT * FROM joueurs"):
    print("joueur :", joueur)
for score in curseur.execute("SELECT * FROM scores"):
    print("score :", score)


connexion.close()
