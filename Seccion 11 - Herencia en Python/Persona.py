class Persona:
  def __init__(self, nombre, edad):
    self.nombre = nombre
    self.edad = edad

class Empleado(Persona):
  def __init__(self, nombre, edad, sueldo):
    super().__init__(nombre, edad)
    self.sueldo = sueldo

empleado_uno = Empleado('Laureano', 18, 45000)
print(empleado_uno.nombre)
print(empleado_uno.edad)
print(empleado_uno.sueldo)