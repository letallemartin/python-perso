class Pile:
    def __init__(self,pile,max_pile):
        self.set_pile(pile)
        self.set_max_pile(max_pile)
        
    def get_pile(self):
        return list(self.pile)
    
    def get_max_pile(self):
        return int(self.max_pile)
    
    def set_pile(self,pile):
        self.pile = pile
    
    def set_max_pile(self,max_pile):
        self.max_pile = max_pile
    
    def est_vide(self):
        return len(self.pile) == 0
    
    def empiler(self,x):
        if len(self.pile) < self.max_pile:
            self.pile.append(x)
        else:
            return None
        
    def depiler(self):
        if len(self.pile)>0:
            self.pile.pop(len(self.pile ) - 1)
        else:
            return None
    
    def __str__(self):
        return( f"{self.pile}")
        
liste=[]       
ma_pile = Pile(liste,5)
ma_pile.empiler(1)
ma_pile.empiler(2)
ma_pile.empiler(3)
ma_pile.empiler(4)
ma_pile.depiler()
ma_pile.depiler()
ma_pile.depiler()
ma_pile.depiler()

print(ma_pile.est_vide())
print(ma_pile)