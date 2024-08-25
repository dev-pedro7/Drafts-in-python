# Herança simples = Relações entre classes
# Assosiação - usa
# Agregação = Tem
# Composição = É dono de
# Herança = É um

class Pessoa:
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome

    def falar_nome_class(self):
        print(self.nome, self.sobrenome, self.__class__.__name__)    

class Cliente(Pessoa):
    ...

class Aluno(Pessoa):
    ...
cli = Cliente('Pedro', 'Silva')
alu = Aluno("Henrique", 'Pedro')
cli.falar_nome_class()
alu.falar_nome_class()
