class Persona:
  contador_personas = 0

  @classmethod
  def generar_valor(cls):
    cls.contador_personas += 1
    return cls.contador_personas

  def __init__(self,nombre,edad):
    self.id = Persona.generar_valor()
    self.name = nombre
    self.age = edad

  def __str__(self):
    return f'Persona [{self.id} {self.name} {self.age}]'


persona1 = Persona('Laureano', 18)
print(persona1)
persona2 = Persona('Lauri', 19)
print(persona2)
print(Persona.contador_personas)