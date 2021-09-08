from dispositivo_entrada import DispositivoEntrada


class Raton(DispositivoEntrada):
    contador_ratones = 0

    def __init__(self, marca, tipo):
        Raton.contador_ratones += 1
        self._id_raton = Raton.contador_ratones
        super().__init__(marca, tipo)

    def __str__(self):
        return f'Id: {self._id_raton}, Marca: {self._marca}, Coneccion: {self._tipo}'


if __name__ == '__main__':
    raton_uno = Raton('BRB', 'USB')
    print(raton_uno)
