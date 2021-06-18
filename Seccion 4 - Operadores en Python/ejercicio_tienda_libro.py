print('Proporcione los isguientes datos del libro: ')
name = input('Nombre: ')
book_id = int(input('ID: '))
price = float(input('Precio: '))
free_ship = input('Envio gratis: ')

print(f'''
  Nombre: {name}
  ID: {book_id}
  Precio: {price}
  Envio Gratis: {free_ship}
''')