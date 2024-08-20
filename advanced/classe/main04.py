class Escritor:
    def __init__(self, nome) -> None:
        self.nome = nome
        self._ferramenta = None

    @property
    def ferramenta(self):
        return self._ferramenta
    @ferramenta.setter
    def ferramenta(self, ferramenta):
        self._ferramenta = ferramenta

class FerramentaEscrever:
    def  __init__(self, nome):
        self.nome = nome        
    def escrever(self):
        return f"{self.nome} esta escrevendo"
    
escritor = Escritor('Pedro')
caneta = FerramentaEscrever('caneta')
maq_escrever = FerramentaEscrever('Maquina')
escritor.ferramenta = maq_escrever
print(caneta.escrever())
print(escritor.ferramenta.escrever())