# with open('./Seccion 21 - Uso de with, resourse/test.txt', 'r', encoding='utf8') as file:
from manejo_archivos import ManejoRecursos
with ManejoRecursos('test.txt') as file:
  print(file.read())