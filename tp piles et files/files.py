class File:
    def __init__(self,file,max_file):
        self.set_file(file)
        self.set_max_file(max_file)
        
    def get_file(self):
        return list(self.file)
    
    def get_max_file(self):
        return int(self.max_file)
    
    def set_file(self,file):
        self.file = file
    
    def set_max_file(self,max_file):
        self.max_file = max_file
    
    def est_vide(self):
        return len(self.file) == 0
    
    def emfiler(self,x):
        if len(self.file) < self.max_file:
            self.file.insert(0,x)
        else:
            return None
        
    def defiler(self):
        if len(self.file)>0:
            self.file.pop(0)
        else:
            return None
    
    def __str__(self):
        return( f"{self.file}")
liste=[]
ma_file = File(liste,5)

ma_file.emfiler(1)
ma_file.emfiler(2)
ma_file.emfiler(3)
print(ma_file)