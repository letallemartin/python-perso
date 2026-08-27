# def factoriel(nbr):
# 	if nbr > 1:
# 		return nbr * factoriel(nbr - 1)
# 	return nbr

# print(factoriel(5))

# def fibonachi(act, prc, n):
# 	if n > 1:
# 		return fibonachi(act + prc, act, n - 1)
# 	return act

# print("actuel = ", fibonachi(1, 0, 15))


# class Carte:
# 	def __init__(self, valeur, couleur):
# 		self.set_couleur(couleur)
# 		self.set_valeur(valeur)
	
# 	def set_valeur(self, valeur):
# 		self.valeur = valeur
	
# 	def get_valeur(self):
# 		return self.valeur
	
# 	def set_couleur(self, couleur):
# 		self.couleur = couleur

# 	def get_couleur(self):
# 		return self.couleur
	
# 	def __str__(self):
# 		return f"{self.valeur}/{self.couleur}"
	
# 	def __gt__(self, other):
# 		return self.valeur > other.valeur
	
# 	def __eq__(self, other):
# 		return self.valeur == other.valeur

# class Paquet:
# 	def	__init__(self):
# 		self.set_paquet()
	
# 	def	set_paquet(self):
# 		self.paquet = [Carte(valeur, couleur) for valeur in range(1, 14) for couleur in ["trefle","as","carreau","coeur"]]

# 	def get_paquet(self):
# 		return str(self.paquet)

# 	def __str__(self):
# 		list = []
# 		for carte in self.paquet:
# 			list.append(str(carte))
# 		return str(list)
	
# 	def melanger(self):
# 		import random
# 		random.shuffle(self.paquet)
	
# 	def piocher(self):
# 		return self.paquet.pop(0)

# carte1 = Carte(4, "pique")
# carte2 = Carte(5, "pique")
# carte3 = Carte(5, "pique")
# print(carte1)
# print(carte1 > carte2)
# print(carte3 == carte2)

# paquet1 = Paquet()
# print(paquet1)
# paquet1.melanger()
# print(paquet1)
# paquet1.piocher()
# print(paquet1)