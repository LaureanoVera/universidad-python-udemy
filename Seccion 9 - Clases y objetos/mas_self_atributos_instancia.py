class Persona:
  def __init__(self, name, last, age):
    self.nombre = name
    self.apellido = last
    self.edad = age

  def mostrar_detalle(self):
    print(f'''
      Nombre: {self.nombre}
      Apellido: {self.apellido}
      Edad: {self.edad}
    ''')

me = Persona('Laureano', 'Vera', 18)
Persona.mostrar_detalle(me)
me.telefono = '+542210000000'
print(me.telefono)