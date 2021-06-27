class Persona:
  def __init__(self, name, last, age):
    self._nombre = name
    self._apellido = last
    self._edad = age

  @property
  def nombre(self):
    print('Llamando metodo get nombre')
    return self._nombre

  @nombre.setter
  def nombre(self, nombre):
    print('Llamando metodo set nombre')
    self._nombre = nombre

  @property
  def apellido(self):
    return self._apellido
    
  @apellido.setter
  def apellido(self, apellido):
    self._apellido = apellido

  @property
  def edad(self):
    return self._edad

  @edad.setter
  def edad(self, edad):
    self._edad = edad

  def __del__(self):
    print(f'Persona: {self.nombre} eliminada')