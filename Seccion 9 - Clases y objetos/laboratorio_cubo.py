class Cubo:
  def __init__(self, ancho, alto, profundo):
    self.x = ancho5
    self.y = alto
    self.z = profundo

  def calcular_volumen(self):
    return self.x * self.y * self.z

ancho = int(input('Proporciona el ancho: '))
alto = int(input('Proporciona el alto: '))
profundo = int(input('Proporciona lo produndo: '))

cubo = Cubo(ancho, alto, profundo)
print(f'Volumen del Cubo: {cubo.calcular_volumen()}')