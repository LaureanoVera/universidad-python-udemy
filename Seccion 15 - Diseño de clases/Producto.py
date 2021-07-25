class Producto:
  contador_productos = 0

  def __init__(self, nombre, precio):
    Producto.contador_productos += 1
    self._id = Producto.contador_productos
    self._nombre = nombre
    self._precio = precio

  def __str__(self):
    return f'Id Producto: {self._id}, Nombre: {self._nombre}, Precio: {self._precio}'

if __name__ == '__main__':
  producto1 = Producto('Remera', 80.00)
  print(producto1)
  producto2 = Producto('Pantalon', 130.00)
  print(producto2)