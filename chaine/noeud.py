class Noeud:
    def __init__(self,valeur,suivant = None):
        self.set_suivant(suivant)
        self.set_valeur(valeur)
        
    def set_valeur(self,valeur):
        self.valeur = valeur
        
    def set_suivant(self,suivant):
        self.suivant = suivant
    
    def get_valeur(self):
        return self.valeur

    def get_suivant(self):
        return self.suivant
    
    def __str__(self):
        return str(self.valeur)

