
import json
#salut je suis ici ca fonctionne 

taches = []
def ajouter_tache (taches , titre):
    tache = {"id" : len(taches)+1 ,"titre" : titre, "terminee" : False}
    
    taches.append(tache)

def afficher_taches (taches):
    for t in taches :
        if t["terminee"] is True:
            print (f"[x] {t['id']} - {t['titre']}")
        else:
            print (f"[ ] {t['id']} - {t['titre']}")
    


def terminer_taches(taches, id):

    trouvee = False

    for t in taches:
        if t['id'] == id :
            t['terminee'] = True
            trouvee = True
    if not trouvee :
        print ("ID introuvable")

def supprimer_taches(taches, id):
    trouvee = False
    for t in taches:
        if t['id'] == id :
            taches.remove(t)
            trouvee = True
    if not trouvee:
        print ("ID introuvable")


def sauvegarder (taches):
    with open ("taches.json","w" ) as f:
        json.dump(taches, f, indent=2)

def charger ():
    try:
        with open ("taches.json",'r') as f:
            return json.load(f)
            
    except FileNotFoundError:
        return []
    
taches = charger()   # charge les tâches au démarrage

while True:
    print("\n=== Gestionnaire de tâches ===")
    print("1. Ajouter une tâche")
    print("2. afficher une tâche")
    print("3. terminer une tâche")
    print("4. suprrimer une tâche")
    print("5. sauvgarder une tâche")

   

    choix = input("Ton choix : ")

    if choix == "1":
        titre = input("Entrer la tache : ")
        ajouter_tache(taches, titre)
    elif choix == "2":

        afficher_taches(taches)
    elif choix == "3":
        id = int(input("Entrer l'ID : "))
        terminer_taches(taches, id)
    elif choix == "4":
        id = int(input("Entrer l'ID : "))
        supprimer_taches(taches, id)
    elif choix == "5":

        sauvegarder(taches)


        print("Au revoir !")
        break


