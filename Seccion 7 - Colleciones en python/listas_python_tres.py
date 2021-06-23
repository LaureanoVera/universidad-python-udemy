names = ['Lauri', 1, 'Ivan', 'Vera', 4]
# largo de una lista
print(len(names))
# agregar un elemento
names.append('Uzumaki')
print(names)
# insertar en indice especifico
names.insert(1, 'Vegeta')
print(names)
# remover elemento
names.remove('Vegeta')
print(names)
# remover el ultimo valor
names.pop()
print(names)
# eliminar elemento en indice indicado
del names[1]
print(names)
# limpiar lista
names.clear()
print(names)