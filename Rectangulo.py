class Rectangulo():
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcularArea(self):
        return self.base * self.altura

# Crear una instancia de Rectangulo con base 6 y altura 4
rectangulo = Rectangulo(6, 4)

# Imprimir el área del rectángulo
print("Área del rectángulo con base {} y altura {} = {} U^2".format(
    rectangulo.base,
    rectangulo.altura,
    rectangulo.calcularArea()
))
