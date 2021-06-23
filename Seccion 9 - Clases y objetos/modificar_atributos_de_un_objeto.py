class Persona:
  def __init__(self, name, last, age):
    self.nombre = name
    self.apellido = last
    self.edad = age

laureano = Persona('Laureano', 'Vera', 18)
print(laureano.nombre)
laureano.nombre = 'Ivan'
laureano.edad = 19
print(laureano.nombre)
print(laureano.edad)