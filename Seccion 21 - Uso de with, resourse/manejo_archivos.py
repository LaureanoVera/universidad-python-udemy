class ManejoRecursos:
  def __init__(self, name):
    self.name = name
    
  def __enter__(self):
    print('Obtenemos el recurso'.center(50,'-'))
    self.name = open(self.name, 'r', encoding='utf8')

  def __exit__(self, tipe_exeption, value_exeption, error_traza):
    print('Cerramos el Recurso'.center(50, '-'))
    if self.name:
      self.name.close()
