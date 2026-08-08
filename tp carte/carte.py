class Carte:
    def __init__(self,valeur,couleur):
        self.set_couleur(couleur)
        self.set_valeur(valeur)

    def get_valeur(self):
        return int(self.valeur)
    
    def get_couleur(self):
        return str(self.couleur)
    
    def set_valeur(self,valeur):
        self.valeur = valeur
    
    def set_couleur(self,couleur):
        self.couleur = couleur
    
    def __str__(self):
        return f"{self.valeur},{self.couleur}"
    
    def __eq__(self,carte2):
        return self.valeur == carte2.valeur

    def __gt__(self,carte2):
        return self.valeur > carte2.valeur
             
        
carte1 = Carte(3,'pique')
# carte2 = Carte(3,'carreau')
# carte3 = Carte(7, 'trèfle')
# print(carte1 == carte2) # Affiche True
# print(carte1 > carte3) # Affiche False
print(carte1)