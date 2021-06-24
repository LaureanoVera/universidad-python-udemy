class Aritmetica:
  """
  Clase Aritmetica para realizar operaciones
  """
  def __init__(self, a, b):
    self.a = a
    self.b = b

  def sumar(self):
    return self.a + self.b

aritmetica = Aritmetica(2, 4)
print(aritmetica.sumar())