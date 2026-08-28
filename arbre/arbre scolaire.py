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

def taille(arbre):
	if arbre is None:
		return 0
	return 1 + taille(arbre.droite) + taille(arbre.gauche)
		
def hauteur(arbre):
	if arbre is None:
		return 0
	return 1 + max(hauteur(arbre.droite) , hauteur(arbre.gauche))

def prefixe(arbre):
	print(arbre.valeur)
	prefixe(arbre.gauche) if arbre.gauche is not None else 0
	prefixe(arbre.droite) if arbre.droite is not None else 0

def infixe(arbre):
	infixe(arbre.gauche) if arbre.gauche is not None else 0
	print(arbre.valeur)
	infixe(arbre.droite) if arbre.droite is not None else 0

def suffixe(arbre):
	suffixe(arbre.gauche) if arbre.gauche is not None else 0
	suffixe(arbre.droite) if arbre.droite is not None else 0
	print(arbre. valeur)

def chercher(arbre,cible):
	if arbre is None:
		return False
	if arbre.valeur == cible:
		return True 
	return chercher(arbre.gauche,cible) or chercher(arbre.droite,cible) 

liste = Noeud('A', 
                Noeud('B', Noeud('D'), Noeud('E')), 
                Noeud('C')
            )
res = hauteur(liste)
print(res)

print(chercher(liste,'C'))