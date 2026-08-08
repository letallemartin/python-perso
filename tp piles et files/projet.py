from piles import Pile

chaine = "())"
def est_bien_parenthesee(chaine):
    ma_pile = Pile([], 100) # On initialise avec une taille max arbitraire
    for cara in chaine:
        if cara == "(":
            ma_pile.empiler(1)
        elif cara == ")":
            if ma_pile.est_vide():
                return False
            else:
                ma_pile.depiler()
    
    return ma_pile.est_vide()

    
print(est_bien_parenthesee(chaine))