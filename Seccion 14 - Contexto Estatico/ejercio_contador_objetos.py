class Persona:
  contador_personas = 0

  def __init__(self,nombre,edad):
    Persona.contador_personas += 1
    self.id = Persona.contador_personas
    self.name = nombre
    self.age = edad

  def __str__(self):
    return f'Persona [{self.id} {self.name} {self.age}]'


persona1 = Persona('Laureano', 18)
print(persona1)