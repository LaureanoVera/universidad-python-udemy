option = None

class TestMovieCatalog:
  def __init__(self):
    pass

while option != 4:
  try:
    print('1. Add Movie')
    print('2. List Movies')
    print('3. Delete Movie Catalog')
    print('4. Exit')
    option = int(input('Select (1-4): '))
  except Exception as e:
      print(f'Errior: {e}')
      option = None
else:
  print('Exit...')