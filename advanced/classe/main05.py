class Carrinho:
    def __init__(self):
        self._produtos = []

    def total(self):
        return sum([p.preco for p in self._produtos])    
    
    def inserir_prod(self, *produtos):
        self._produtos += produtos
    
    def list_produtos(self):
        for produtos in self._produtos:
            print (produtos.nome, produtos.preco)

class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

carrinho = Carrinho()                
p1, p2 = Produto('Caneta', 1.20), Produto('Camiseta', 20)
carrinho.inserir_prod(p1,p2)
print()
print('Produtos inseridos:')
carrinho.list_produtos()
print("R$", carrinho.total())
print()