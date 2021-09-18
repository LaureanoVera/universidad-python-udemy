# try:
#   file = open('./Seccion 20 - Manejo de Archivos/test.txt', 'r')
#   # print(file.read())
#   # print(file.read(4))
#   # print(file.readline())
# except Exception as e:
#   print(e)
# finally:
#   file.close()
#   print('\n')
#   print('Close file')

file = open('./Seccion 20 - Manejo de Archivos/test.txt', 'r')
file_two = open('./Seccion 20 - Manejo de Archivos/copy.txt', 'a')

# # iterar el archivo
# for line in file:
#   print(line)

# a - anexar informacion
file_two.write(file.read())
file_two.close()
print('End Proccess')