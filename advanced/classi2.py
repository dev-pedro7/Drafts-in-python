class Cara:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
d1 = Cara('atumalka', 15)
print(d1.__dict__)        

d1.idade = 120
d1.__dict__['outro'] = 'coiso'
print(vars(d1))        

          
class Person:

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    @classmethod    
    def anom(cls, nome):
        return cls(nome , 15)

dados = {'nome': 'João', 'idade': 35}
d2 = Person(**dados)
d3 = Person.anom('pedro')
print(vars(d2))
print(vars(d3))


#@Property
class TheBest:
    def __init__(self, jogador):
        self.player = jogador

    @property
    def jogador(self):
        print('properthy JOGADOR')
        return self.player
    
    # def get_jogador(self):
    #     # print('GET JOGADOR')
    #     # return self.player
    

joga = TheBest('Messi')        
print(joga.jogador)        


# @property + @setter - getter e setter no modo Pythônico
# - como getter
# - p/ evitar quebrar código cliente
# - p/ habilitar setter
# - p/ executar ações ao obter um atributo
# Atributos que começar com um ou dois underlines
# não devem ser usados fora da classe.
#  🐍🤓🤯🤯🤯🤯
class Caneta:
    def __init__(self, cor):
        # private protected
        self.cor = cor
        self._cor_tampa = None
        self.lagarto = None

    @property
    def cor(self):
        print('ESTOU NO GETTER')
        return self._cor

    @cor.setter
    def cor(self, valor):
        print('ESTOU NO SETTER')
        self._cor = valor

    @property
    def cor_tampa(self):
        return self._cor_tampa

    @cor_tampa.setter
    def cor_tampa(self, valor):
        self._cor_tampa = valor


caneta = Caneta('Azul')
caneta.cor = 'Rosa'
caneta.cor_tampa = 'Azul'
print(caneta.cor)
print(caneta.cor_tampa)


# class Jacare:
#     def __init__(self, raca):
#         self.crocodilo = raca

#     @property
#     def raca(self):
#         print('PROPERTY')
#         return self.raca

#     @raca.setter    
#     def raca(self):
    


# f = Jacare('aligator')    
# print(f.crocodilo)    
# print(f.raca)    
print('b')