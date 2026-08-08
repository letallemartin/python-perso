from carte import Carte
class Paquet:
    def __init__(self):
        self.set_paquet()
        
    def set_paquet(self,):
        self.paquet = [Carte(valeur,couleur) for valeur in range (1,14) for couleur in ['pique', 'carreau', 'trefle', 'coeur']]
        
    def get_paquet(self):
        return list(self.paquet)
    
    def __str__(self):
        new_paquet = [str(carte) for carte in self.paquet]
        return f"{new_paquet}"
    
    def melanger(self):
        import random
        random.shuffle(self.paquet)
    
    def piocher(self):
        carte = self.paquet.pop(0)
        return carte
            
            
   