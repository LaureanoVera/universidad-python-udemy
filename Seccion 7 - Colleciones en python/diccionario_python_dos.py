dictionary = {
  'IDE': 'Integrated Development Environment',
  'OPP': 'Object Oriented Programming',
  'DBMS': 'DataBase Managment System'
}
# recorrer elementos
for term, value in dictionary.items():
  print(term, value)

for term in dictionary.keys():
  print(term)

for value in dictionary.values():
  print(value)

# comprobar existencia de algun elemento
print('IDE' in dictionary)
# agregar elemento
dictionary['PK'] = 'Primary Key'
print(dictionary)
# remover un elemento
dictionary.pop('DBMS')
print(dictionary)
# limpiar
dictionary.clear()
print(dictionary)
# eliminar
del dictionary