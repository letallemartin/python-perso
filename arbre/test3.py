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
    
    def get_suivant(self):
        return self.enfant
    
    def est_vide(liste):
        return len(liste) == 0
    
    def make_arbre(liste):
        if not Noeud.est_vide(liste):
            nouv1 = Noeud(liste[0])
            if len(liste) > 1:
                for elem in liste[1]:
                    nouv2 = Noeud.make_arbre(elem)
                    nouv1.enfant.append(nouv2)
        return nouv1
    
    
    
liste = ["debut",[["village",[["maison"],["marche"]]],["foret",[["arbre"],["vielle homme"]]]]]

mon_arbre = Noeud.make_arbre(liste)
print(mon_arbre.get_valeur())               # Affiche: debut
print(mon_arbre.enfant[0].get_valeur())      # Affiche: village
print(mon_arbre.enfant[1].get_valeur())      # Affiche: foret