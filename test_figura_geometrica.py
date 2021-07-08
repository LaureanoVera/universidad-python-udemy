from FiguraGeometrica2 import Cuadrado

cuadrado_uno = Cuadrado(5, 'rojo')
print(cuadrado_uno.calcular_area())

# MRO - Method Resolution Order
print(Cuadrado.mro())