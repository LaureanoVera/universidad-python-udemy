from Producto import Producto

class Orden:
  contador_ordenes = 0
  def __init__(self, productos):
    Orden.contador_ordenes += 1
    self._id = Orden.contador_ordenes
    self._productos = list(productos)

  def agregar_producto(self, producto):
    self._productos.append(producto)

  def calcular_total(self):
    total = 0
    for producto in self._productos:
      total += producto.precio
    return total

  def __str__(self):
    self.productos_str = ""
    for producto in self._productos:
      self.producto_str += producto.__str__() + '|'

    return f'Orden: {self._id}'

if __name__ == '__main__':
  producto1 = Producto('Remera', 80.00)
  producto2 = Producto('Pantalon', 130.00)
  productos1 = [producto1, producto2]
  orden1 = Orden(producto1)
  print(orden1)