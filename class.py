class CompteBancaire:
    """Un compte bancaire simple."""

    def __init__(self, titulaire, solde=0):
        # __init__ s'exécute à la création de l'objet
        self.titulaire = titulaire  # attribut
        self.solde     = solde      # attribut

    def deposer(self, montant):
        self.solde += montant
        print(f"Dépôt de {montant}$ → solde : {self.solde}$")

    def retirer(self, montant):
        if montant > self.solde:
            print("Solde insuffisant")
            return
        self.solde -= montant
        print(f"Retrait de {montant}$ → solde : {self.solde}$")

    def __str__(self):
        # s'exécute quand tu fais print(objet)
        return f"Compte de {self.titulaire} — {self.solde}$"

# Créer des objets (instances)
alice = CompteBancaire("Alice", 1000)
bob   = CompteBancaire("Bob")

alice.deposer(500)    # Dépôt de 500$ → solde : 1500$
alice.retirer(200)   # Retrait de 200$ → solde : 1300$
bob.deposer(100)     # Dépôt de 100$ → solde : 100$
print(alice)          # Compte de Alice — 1300$