class Cliente:
    def __init__(self, nome):
        self.nome = nome
        self.enderecos = []

    def inserir_enderecos(self, rua, numero):
        self.enderecos.append(Endereco(rua,numero))

    def listar_enderecos(self):
        for endereco in self.enderecos:
            print(endereco.rua, endereco.numero)


class Endereco:
    def __init__(self, rua, numero):
        self.rua = rua
        self.numero = numero

client = Cliente('Pedro')
client.inserir_enderecos("Ibirapuera", 13)
client.inserir_enderecos('Boa vista', 50)

client.listar_enderecos()
#print(client.enderecos[0].rua)
#print(client.enderecos[1].rua)
