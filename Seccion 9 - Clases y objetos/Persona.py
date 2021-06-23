class Persona:
  mi_atributo = ''
  def __init__(self):
    self.nombre = 'Laureano'
    self.apellido = 'Vera'
    self.edad = 18

persona1 = Persona()
print(type(Persona))
print(persona1.nombre)
print(persona1.apellido)
print(persona1.edad)