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

laureano = Persona('Laureano', 'Vera', 18)
laureano.mostrar_detalle()
print(laureano.edad)