class Carte:
    def __init__(self,valeur,couleur):
        self.set_valeur(valeur)
        self.set_couleur(couleur)
    
    def set_valeur(self,valeur):
        assert isinstance(valeur,int)
        self.valeur = valeur
    
    def set_couleur(self,couleur):
        assert isinstance(couleur,str)
        self.couleur = couleur
    
    def get_valeur(self):
        return self.valeur
    
    def get_couleur(self):
        return self.couleur
    
    def __str__(self):
        return f"{self.valeur}/{self.couleur}"
    
    def __eq__(self,autre):
        return self.valeur == autre.valeur
    
    def __gt__(self,autre):
        return self.valeur > autre.valeur
    
class Paquet:
    def __init__(self,paquet):
        self.set_paquet(paquet)
    
    def set_paquet(self,paquet):
        if paquet is None:
            self.paquet =[]
        elif isinstance(paquet,list):
            self.paquet = paquet
        else:
            self.paquet = [paquet]
    
    def get_paquet(self):
        return self.paquet
    
    def __str__(self):
        liste = []
        for elem in self.paquet:
            liste.append(str(elem))
        return str(liste)
            
    
carte1 = Carte(2,"pique")
carte2 = Carte(4,"pique")
print(carte1)
print(carte1 == carte2 )
print(carte2 > carte1)
paquet1 = [Carte(valeur,couleur) for valeur in range(1,14) for couleur in ["Pique","Trefle","Carreau","Coeur"]]
mon_paquet = Paquet(paquet1)
print(mon_paquet)
