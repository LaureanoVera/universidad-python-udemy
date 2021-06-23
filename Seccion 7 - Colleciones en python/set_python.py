# set
planets = {'mars', 'jupiter', 'venus'}
print(planets)
# largo
print(len(planets))
# revisar si un elemento esta presente
print('saturn' in planets)
# agregar elemento
planets.add('earth')
print(planets)
# no se pueden duplicar elementos
planets.add('earth')
print(planets)
# eliminar elementos
planets.remove('earth')
print(planets)
planets.discard('venus')
print(planets)
# limpiar set
planets.clear()
print(planets)
# eliminar set
del planets
# print(planets)