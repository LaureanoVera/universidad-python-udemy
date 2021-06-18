print('### Ejercicio rango ###')
value = int(input('Writte value: '))
min_value = 0
max_value = 5
within_range = (value >= min_value) and (value <= max_value)
if within_range:
  print(f'the value of {value} is within the range')
else:
  print(f'the value of {value} is not within the range')
print('### ##### ### ##### ###')