try:
  file = open('./Seccion 20 - Manejo de Archivos/test.txt', 'r')
  # print(file.read())
  # print(file.read(4))
  print(file.readline())
  print(file.readline())
except Exception as e:
  print(e)
finally:
  file.close()
  print('\n')
  print('Close file')