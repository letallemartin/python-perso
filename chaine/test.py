class Noeud:
    def __init__(self,valeur,suivant = None, parent = None):
        self.set_valeur(valeur)
        self.set_suivant(suivant)
        self.set_parent(parent)
    
    
    def set_valeur(self,valeur):
        self.valeur = valeur
    
    def set_suivant(self,suivant):
        if suivant is None:
            self.suivant = []
        else:
            self.suivant = [suivant]
            
    
    def set_parent(self,parent):
        self.parent = parent
    
    def get_valeur(self):
        return self.valeur
    
    def get_suivant(self):
        return self.suivant
    
    def get_parent(self):
        return self.parent
    
    def __str__(self):
        return str(self.valeur)
    

class Chaine:
    def __init__(self,liste = None):
        self.set_liste(liste)
        

    def set_liste(self,liste):
        self.liste = liste
        
    def get_liste(self):
        return self.liste
    
    def est_vide(self):
        return self.liste == None
    
    def insert_niveau(self,liste): 
        nouv = Noeud(liste[0])
        if len(liste) > 1:
            for elem in liste[1]:
                sous_nouv = self.insert_niveau(elem)
                sous_nouv.parent = nouv
                nouv.suivant.append(sous_nouv) 
        return nouv       
                
                
    def __str__(self):
        # if self.est_vide(): 
        #     return "Chaîne vide"
        
        # def afficher(noeud, indentation=""):
        #     txt = f"{indentation}[{noeud.valeur}]\n"
        #     for choix in noeud.suivant:
        #         txt += afficher(choix, indentation + "  |--- ")
        #     return txt
            
        # return "--- ARBRE DE CHOIX ---\n" + afficher(self.liste)
       pass 
                
        
    
   
    
liste = ["debut",[["village",[["maison"],["marche"]]],["foret",[["arbre"],["vielle homme"]]]]]
ma_chaine = Chaine()
# Remplace ta ligne par celle-ci :
ma_chaine.set_liste(ma_chaine.insert_niveau(liste))
print(ma_chaine)

