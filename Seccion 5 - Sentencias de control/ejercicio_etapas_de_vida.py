age = int(input('Edad:'))
text_print = ''

if age >= 0 and age <= 10:
  text_print = 'La infancia es increible'
elif age >= 11 and age <= 20:
  text_print = 'Muchos cambios y mucho estudio...'
elif age >= 21 and age <= 30:
  text_print = 'Amor y comienza el trabajo'
else:
  text_print = 'Sin datos actualmente'

print(text_print)