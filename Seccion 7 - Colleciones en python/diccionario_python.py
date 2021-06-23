# dict (key, value)
dictionary = {
  'IDE': 'Integrated Development Environment',
  'OPP': 'Object Oriented Programming',
  'DBMS': 'DataBase Managment System'
}
print(dictionary)
# largo
print(len(dictionary))
# acceder a un elemento
print(dictionary['OPP'])
# otra forma de recuperar un elemento
print(dictionary.get('OPP'))
# modificando elementos
dictionary['IDE'] = 'Integrated DEVELOPMENT Environment'
print(dictionary)