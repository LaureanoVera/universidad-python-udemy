class Persona:
  def __init__(self, name, last, age):
    self.nombre = name
    self.apellido = last
    self.edad = age

naruto = Persona('Naruto', 'Uzumaki', 13)
sasuke = Persona('Sasuke', 'Uchiha', 13)
kankuro = Persona('Kankuro', '???', 14)

print(naruto.nombre)
print(sasuke.nombre)
print(kankuro.nombre)