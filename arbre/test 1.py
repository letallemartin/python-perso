class Noeud:
    def __init__(self,valeur,enfant = None):
        self.set_valeur(valeur)
        self.set_enfant(enfant)
        
    def set_valeur(self,valeur):
        self.valeur = valeur
    
    def set_enfant(self,enfant):
        if enfant == None:
            self.enfant = []
        elif isinstance(enfant,list):
            self.enfant = enfant
        else:
            self.enfant = [enfant]
    
    def get_valeur(self):
        return self.valeur
    

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
                for elem in self.liste1[1]:
                    newlist = Arbre(elem)
                    nouv2 = newlist.make_arbre()
                    nouv1.enfant.append(nouv2)
        else:
            nouv1 = None
        return nouv1 
    
    def taille(self, x=1):
            if len(self.liste1) > 1:
                for elem in self.liste1[1]:
                    nouv2 = Arbre(elem)
                    nouv2.make_arbre()
                    x += nouv2.taille()
            return x
            
        
liste = ["debut",[["village",[["maison"],["marche"]]],["foret",[["arbre"],["vielle homme"]]]]]
mon_arbre = Arbre(liste)

mon_arbre.make_arbre()
print(mon_arbre.taille())
