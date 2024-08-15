class  Pessoa:
    def __init__(self, nome, sobrenome, walks=False):
        self.nome = nome
        self.sobrenome = sobrenome
        self.walks = walks

    def walk(self):
        if self.walks:
            print(f'{p1.nome} JÁ esta andando')
            return
        
        print(f'{p1.nome} esta andando')
        self.walks = True

p1 = Pessoa('Pedro', "Henrique")
print(p1.nome, p1.sobrenome)
p1.walk()
p1.walk()