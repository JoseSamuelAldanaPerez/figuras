# Aldana Pérez José Samuel 20240446

class Triangulo():
  def __init__(self, base, altura):
    self.base = base
    self.altura = altura

  def calcularArea(self):
    return (self.base * self.altura) / 2;

triangulo = Triangulo(3, 8)
print("Área del triangulo: ({}x{})/2 = {} U2".format(
  triangulo.base,
  triangulo.altura,
  triangulo.calcularArea()
))