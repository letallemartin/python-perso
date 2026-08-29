class Noeud:
	def __init__(self, valeur, suivant = None):
		self.set_valeur(valeur)
		self.set_suivant(suivant)

	def set_valeur(self, valeur):
		self.valeur = valeur
	
	def set_suivant(self, suivant):
		self.suivant = suivant
	
	def get_valeur(self):
		return self.valeur
	
	def get_suivant(self):
		return self.suivant
	
	def __str__(self):
		liste = []
		actuel = self
		while actuel != None:
			liste.append(actuel.valeur)
			actuel = actuel.suivant
		return str(liste)

def add_debut(tete, valeur):
	tete = Noeud(valeur, tete)
	return tete

def add_fin(tete, valeur):
	if tete is None:
		tete = Noeud(valeur, None)
	else:
		actuel = tete
		while actuel.suivant != None:
			actuel = actuel.suivant
		actuel.suivant = Noeud(valeur, None)
	return tete
liste = None
liste = add_debut(liste, "a")
liste = add_debut(liste, "b")
liste = add_debut(liste, "c")
liste = add_fin(liste, "d")
actuel = liste
# while actuel.suivant != None:
# 	print(actuel.valeur)
# 	actuel = actuel.suivant

print(liste)