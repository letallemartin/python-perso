class Noeud:
    def __init__(self,valeur,gauche = None, droite = None):
        self.set_valeur(valeur)
        self.set_gauche(gauche)
        self.set_droite(droite)
        
    def set_valeur(self,valeur):
        self.valeur = valeur
    
    def set_gauche(self,gauche):
        self.gauche = gauche
    
    def set_droite(self,droite):
            self.droite = droite
    
    def get_valeur(self):
        return self.valeur
    
    def get_droite(self):
            return self.droite
        
    def get_gauche(self):
            return self.gauche
    

class Arbre:
    def __init__(self,liste1 = None):
        self.set_liste1(liste1)
        
    def set_liste1(self,liste1):
        if liste1 == None:
            self.liste1 = []
        elif isinstance(liste1,list):
            self.liste1 = liste1
        else:
            self.liste1 = [liste1]
        
    def get_liste1(self):
        return list(self.liste1)
    
    def est_vide(self):
        return len(self.liste1) == 0
    
    def make_arbre(self):
        if not self.est_vide():
            nouv1 = Noeud(self.liste1[0])
            if len(self.liste1 ) > 1:
                newlist = Arbre(self.liste1[1])
                nouv2 = newlist.make_arbre()
                nouv1.gauche = nouv2
            if len(self.liste1 ) > 2:
                newlist = Arbre(self.liste1[2])
                nouv3 = newlist.make_arbre()
                nouv1.droite = nouv3
        else:
            nouv1 = None
        return nouv1 
    
    # def taille(self, x=1):
    #         if len(self.liste1) > 1:
    #             for elem in self.liste1[1]:
    #                 nouv2 = Arbre(elem)
    #                 nouv2.make_arbre()
    #                 x += nouv2.taille()
    #         return x
            
        
liste = [
    'A', 
    ['B', ['D', None, None], ['E', None, None]], 
    ['C', None, None]
]
mon_arbre = Arbre(liste)

mon_arbre.make_arbre()

