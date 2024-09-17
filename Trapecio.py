class Trapecio:
    class Trapecio():
        def __init__(self, base, base2, altura):
            self.base = base
            self.base2 = base2
            self.altura = altura
    
        def calcularArea(self):
            return  ((self.base + self.base2) * self.altura) / 2

    trapecio = Trapecio(3,4,5)
    print("Área del trapecio con base uno {} , trapecio con base2 {} y altura {} = {} U^2".format(
        trapecio.base,
        trapecio.base2,
        trapecio.altura,
        trapecio.calcularArea()
    ))
