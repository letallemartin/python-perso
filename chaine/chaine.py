from noeud import Noeud

class ListeChainer:
    def __init__(self,tete = None):
        self.set_tete(tete)
        
    def set_tete(self,tete):
        self.tete = tete
    
    def get_tete(self):
        return self.tete
    
    def est_vide(self):
        return self.tete == None
    
    def insérer_au_début(self,valeur):
        self.tete = Noeud(valeur,self.tete)
        
    def insérer_à_la_fin(self,valeur):
        if self.est_vide():
            self.tete = Noeud(valeur,self.tete)
        else:
            actuel = self.tete
            while actuel.suivant != None:
                actuel = actuel.suivant
            actuel.suivant = Noeud(valeur,actuel.suivant)
            
        
    
    def __str__(self):
        liste = []
        actuel = self.tete
        while actuel != None:
            liste.append(actuel.valeur)
            actuel = actuel.suivant
        return str(liste)
    