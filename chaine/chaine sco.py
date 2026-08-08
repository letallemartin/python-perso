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
    
    def __str__(tete):
        liste = []
        actuel = tete
        while actuel != None:
            liste.append(actuel.valeur)
            actuel = actuel.suivant
        return str(liste)

    
def est_vide(tete):
    return tete == None
    
def insérer_au_début(tete,valeur):
    return Noeud(valeur,tete)
        
def insérer_à_la_fin(tete,valeur):
    if tete is None:
        return Noeud(valeur)
    else:
        actuel = tete
        while actuel.suivant != None:
            actuel = actuel.suivant
        actuel.suivant = Noeud(valeur,None)
    return tete
            
def taille(tete):
    count = 0
    actuel = tete
    while actuel != None:
        actuel = actuel.suivant
        count += 1
    return count
    
# commentaire
    

liste = None
liste = insérer_au_début(liste ,1)
liste =insérer_au_début(liste,2)
liste = insérer_au_début(liste,3)
liste = insérer_à_la_fin(liste,80)
if not est_vide(liste):
    print(liste)
print(taille(liste))

