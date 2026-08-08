class Noeud:
    def __init__(self,valeur,suivant = None):
        self.set_valeur(valeur)
        self.set_suivant(suivant)
        
    def set_valeur(self,valeur):
        self.valeur = valeur
    
    def set_suivant(self,suivant):
        if suivant == None:
            self.suivant = []
        elif isinstance(suivant, list):
            self.suivant = suivant
        else:
            self.suivant = [suivant]
    
    def get_valeur(self):
        return self.valeur
    
    def get_suivant(self):
        return self.suivant
    
class Arbre:
    def __init__(self,liste1 = None):
        self.set_liste1(liste1)
        self.racine = self.make_arbre()
        
    def set_liste1(self,liste1):
        if liste1 == None:
            self.liste1 = []
        elif isinstance(liste1, list):
            self.liste1 = liste1
        else:
            self.liste1 = [liste1]
        
    def get_liste1(self):
        return list(self.liste1)
    
    def est_vide(self):
        return len(self.liste1) == 0
    
    def make_arbre(self):
        if not self.est_vide():
            nouv = Noeud(self.liste1[0])
            if len(self.liste1) > 1:
                for elem in self.liste1[1]:
                    new_liste1 = Arbre(elem)
                    sous_nouv = new_liste1.make_arbre()
                    nouv.suivant.append(sous_nouv)
        return nouv
                    
    def __str__(self):
        return f"{self.liste1},{self.taille_liste1()}"
    
    def taille_liste1(self,x = 1):
        if len(self.liste1) > 1:
            for elem in self.liste1[1]:
                new_liste1 = Arbre(elem)
                new_liste1.make_arbre()
                x += new_liste1.taille_liste1()
        return x
            
liste = ["debut",[["village",[["maison"],["marche"]]],["foret",[["arbre"],["vielle homme"]]]]]

moi = Arbre(liste)
print(moi.taille_liste1())      
    
    
    