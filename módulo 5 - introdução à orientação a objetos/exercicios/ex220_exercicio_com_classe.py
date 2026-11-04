class Carro:
    def __init__(self, nome):
        self.nome = nome
        self._motor = None
        self._fabricante = None
    
    #GETTERS E SETTERS
    @property
    def carro(self):
        return self.nome    

    @property
    def inserir_motor(self):
        return self._motor

    @inserir_motor.setter
    def inserir_motor(self, motor):
        self._motor = motor
    
    @property
    def inserir_fabricante(self):
        return self._fabricante
    
    @inserir_fabricante.setter
    def inserir_fabricante(self, fabricante):
        self._fabricante = fabricante


class Motor:
    def __init__(self, nome):
        self.nome = nome

class Fabricante:
    def __init__(self, nome):
        self.nome = nome

car1 = Carro("New bettle")
fab1 = Fabricante("Volkswagen")
mot1 = Motor("V8")
car1.inserir_fabricante = fab1
car1.inserir_motor = mot1
print("Informações do carro 1\n", f"Fabricante: {car1.inserir_fabricante.nome}, Carro: {car1.carro}, Motor: {car1.inserir_motor.nome}")
print()
print()

car2 = Carro("Uno")
fab2 = Fabricante("Ford")
car2.inserir_motor = mot1
car2.inserir_fabricante = fab2
print("Informações do carro 2\n", f"Fabricante: {car2.inserir_fabricante.nome}, Carro: {car2.carro}, Motor: {car2.inserir_motor.nome}")