import json
caminho_arquivo = 'C:\\Users\\Pedro\\Documents\\Python\\mid\\'
caminho_arquivo += 'salvando_class.json'
class Cara:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
d1 = Cara('pedrin', 15)
      

with open('salvando_class.json', 'w') as arquivo:
    json.dump(d1.__dict__, arquivo)