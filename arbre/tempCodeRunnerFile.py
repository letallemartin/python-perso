def chercher(self,cible):
        if self.valeur ==  cible:
            return True
        elif self.valeur is None:
            return False
        return self.gauche.chercher(cible) or self.droite.chercher(cible)