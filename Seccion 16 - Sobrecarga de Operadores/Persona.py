class Persona:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def __add__(self, other):
    return f'{self.name} {other.name}'

  def __sub__(self, other):
    return self.age - other.age

persona1 = Persona('Laureano', 18)
persona2 = Persona('Ivan', 19)
print(persona1 + persona2)
print(persona1 - persona2)

# obj1 + obj2
# obj1.__add__(obj2)