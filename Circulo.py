#Diego Muñoz Rodriguez

import math

class Circulo():
    def __init__(self, radio):
        self.radio = radio

    def calcularArea(self):
        return math.pi * (self.radio ** 2)

# Crear una instancia de Circulo con un radio de 5
circulo = Circulo(5)

# Imprimir el área del círculo
print("Área del círculo con radio {} = {:.2f} U²".format(
    circulo.radio,
    circulo.calcularArea()
))
