class Persona:
  def __init__(self, name, last, age):
    self._nombre = name
    self.apellido = last
    self.edad = age

laureano = Persona('Laureano', 'Vera', 18)
print(laureano.edad)