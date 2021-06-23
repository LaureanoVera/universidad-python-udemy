class Persona:
  def __init__(self, name, last, age):
    self.nombre = name
    self.apellido = last
    self.edad = age

laureano = Persona('Laureano', 'Vera', 18)
print(laureano.edad)