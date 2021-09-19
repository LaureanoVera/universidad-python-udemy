from domain.movie import Movie
from service.movie_catalog import MovieCatalog as MC

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

    if option == 1:
      movie_name = input('Movie Name: ')
      movie = Movie(movie_name)
      MC.add_movie(movie)
    elif option == 2:
      MC.list_movie()
    elif option == 3:
      MC.delete_movie()
      
  except Exception as e:
      print(f'Errior: {e}')
      option = None
else:
  print('Exit...')