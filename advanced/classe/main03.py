class Cor:
    def __init__(self, cor):
        self.cor_tinta = cor
    
    @property
    def core(self):
        print('property')
        return self.cor_tinta
    
    @property
    def cor_iris(self):
        return '2'

cores = Cor('Azul')
print(cores.core)
print(cores.core)        
print(cores.core)        
print(cores.core)        
print(cores.cor_iris)        



    

