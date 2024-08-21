class Carro:
    def __init__(self, car_name):
        self.car_name = car_name
        self._motor = None
        self._fabricante = None


    @property
    def motor(self):
        return self._motor
    @motor.setter
    def motor(self, motor):
        self._motor = motor

    @property
    def fabricante(self):
        return self._fabricante
    @fabricante.setter
    def fabricante(self, fabricante):
        self._fabricante = fabricante
        
class Motor:
    def __init__(self, nome):
        self.nome = nome
    
class Fabricante:
    def __init__(self, nome):
        self.nome = nome
    
carro = Carro('Civic')
fabricante = Fabricante('Honda')
motor = Motor('V8')
carro.fabricante = fabricante 
carro.motor = motor
print(carro.fabricante.nome, carro.car_name, carro.motor.nome)


