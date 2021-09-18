try:
  file = open('./Seccion 20 - Manejo de Archivos/test.txt', 'w', encoding='utf8')
  file.write('Add information here')
  file.write('\n')
  file.write('New line')
except Exception as e:
  print(e)
finally:
  file.close()
  print('Close file')