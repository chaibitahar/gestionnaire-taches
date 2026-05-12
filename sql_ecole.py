import sqlite3
connexion = sqlite3.connect(r"C:\Users\chaib\Desktop\dev\ecole.db")
curseur = connexion.cursor()

curseur.execute("SELECT nom, prenom, email FROM etudiants")

etudiants = curseur.fetchall()

for etudiant in etudiants :
    print(f"Nom :{etudiant[0]} {etudiant[1]} --Email: {etudiant[2]}")

curseur.execute("""
    SELECT etudiants.nom, etudiants.prenom, notes.note, cours.nom_cours
    FROM notes
    INNER JOIN etudiants ON notes.id_etudiant = etudiants.id
    INNER JOIN cours ON notes.id_cours = cours.id
""")
resultats = curseur.fetchall()
for r in resultats:
    print(f"{r[0]} {r[1]} — {r[3]} : {r[2]}/100")




connexion.close()
