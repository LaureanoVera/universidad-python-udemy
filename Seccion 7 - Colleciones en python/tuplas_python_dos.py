fruits = ('apple', 'orange', 'pear')
# recorrer elementos
for fruit in fruits:
  print(fruit, end=' ')
# cambiar valor de tupla
# fruits[1] = 'banana' # !
fruitsList = list(fruits)
fruitsList[1] = 'banana'
fruits = tuple(fruitsList)
print('\n',fruits)
# eliminar tupla
del fruits
# print(fruits)