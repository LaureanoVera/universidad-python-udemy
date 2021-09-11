from teclado import Teclado
from raton import Raton
from monitor import Monitor

class Computadora:
  contador_computadoras = 0
  def __init__(self, nombre, monitor, teclado, raton):
    Computadora.contador_computadoras += 1
    self._id_computadora = Computadora.contador_computadoras
    self._nombre = nombre
    self._monitor = monitor
    self._teclado = teclado
    self._raton = raton

  def __str__(self):
    return f'''
    {self._nombre}: {self._id_computadora}
    Monitor: {self._monitor}
    Teclado: {self._teclado}
    Raton: {self._raton}
    '''

if __name__ == '__main__':
  monitor = Monitor('AOC', 19)
  teclado = Teclado('BRB', 'USB')
  raton = Raton('BRB', 'USB')
  computadora = Computadora('Monstruosa', monitor, teclado, raton)
  print(computadora)