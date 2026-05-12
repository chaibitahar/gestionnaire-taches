from collections import deque

class SupportTechnique:
    def __init__(self):
        self.fille = deque()
    
    def ajouter_ticket(self, client):
        self.fille.append(client)
    
    def traiter_ticket(self):
        if len (self.fille) == 0 :
            print("Aucun ticket en attente")
            return
        premier_client = self.fille.popleft()
        print (f"Traitement du ticket de : {premier_client}")
    def afficher_file(self):
        print("file :"+"->".join(self.fille))
            

        
        


    



support = SupportTechnique()
support.ajouter_ticket("Alice")
support.ajouter_ticket("Bob")
support.ajouter_ticket("Cara")
support.afficher_file()
# File : Alice → Bob → Cara

support.traiter_ticket()
# Traitement du ticket de : Alice

support.afficher_file()
# File : Bob → Cara


        