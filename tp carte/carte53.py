class Carte:
    def __init__(self,valeur,couleur):
        self.set_valeur(valeur)
        self.set_couleur(couleur)
    
    def set_valeur(self,valeur):
        self.valeur = valeur 
    
    def set_couleur(self,couleur):
        self.couleur = couleur
    
    def get_valeur(self):
        return self.valeur
    
    def get_couleur(self):
        return self.couleur
    
    def __str__(self):
        return f"{self.valeur},{self.couleur}"
    
    def __gt__(self,autre):
        return self.valeur > autre.valeur
    
    def __eq__(self,autre):
        return self.valeur == autre.valeur

class Paquet:
    def __init__(self):
        self.set_paquet()
    
    def set_paquet(self):
        self.paquet = [Carte(valeur,couleur) for valeur in range(1,14) for couleur in ("trefle","as","carreau","coeur") ]
    
    def get_paquet(self):
        return self.paquet
    
    def __str__(self):
        liste = []
        for elem in self.paquet:
            liste.append(str(elem))
        return str(liste)
    
    def melanger(self):
        import random
        random.shuffle(self.paquet)
    
    def piocher(self):
        carte = self.paquet.pop(0)
        return carte
 
carte1 = Carte(4,"carreau")
carte2 = Carte(3,"carreau")
print(carte1>carte2)
paquet1 = Paquet()
print(paquet1)
