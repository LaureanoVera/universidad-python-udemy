class Persona:
  def __init__(self, name, last, age):
    self._nombre = name
    self.apellido = last
    self.edad = age

  @property
  def nombre(self):
    print('Llamando metodo get nombre')
    return self._nombre

  # @nombre.setter
  # def nombre(self, nombre):
  #   print('Llamando metodo set nombre')
  #   self._nombre = nombre

laureano = Persona('Laureano', 'Vera', 18)
print(laureano.nombre)
laureano.nombre = 'Lauri'
print(laureano.nombre)