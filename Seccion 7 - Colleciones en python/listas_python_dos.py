names = ['Lauri', 1, 'Ivan', 'Vera', 4]
# imprimir un rango
print(names[2:4])
# ir de inicio lista al indice (sin incluirlo)
print(names[:3])
# desde indice hasta el final
print(names[1:])
# cambiar un valor
names[1] = 'Goku'
names[4] = 'Uchiha'
print(names)  
# iterar una lista
for name in names:
  print(name)