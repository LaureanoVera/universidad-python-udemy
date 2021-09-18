import os

class MovieCatalog:
  file_route = 'movies.txt'

  @classmethod
  def add_movie(cls, movie):
    with open(cls.file_route, 'a', encoding='utf8') as file:
      file.write(f'{movie.name}\n')

  @classmethod
  def list_movie(cls):
    with open(cls.file_route, 'r', encoding='utf8') as file:
      print('Movie Catalog'.center(50, '-'))
      print(file.read())

  @classmethod
  def delete_movie(cls):
    os.remove(cls.file_route)
    print(f'Delete File: {cls.file_route}')


  # def __init__(self):
