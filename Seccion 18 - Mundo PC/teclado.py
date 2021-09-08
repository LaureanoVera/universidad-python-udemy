from dispositivo_entrada import DispositivoEntrada

class Teclado(DispositivoEntrada):
    contador_teclados = 0

    def __init__(self, marca, tipo):
        Teclado.contador_teclados += 1
        self._id_teclado = Teclado.contador_teclados
        super().__init__(marca, tipo)

    def __str__(self):
        return f'Id: {self._id_teclado}, Marca: {self._marca}, Coneccion: {self._tipo}'


if __name__ == '__main__':
    teclado_uno = Teclado('Razer', 'USB')
    print(teclado_uno)
