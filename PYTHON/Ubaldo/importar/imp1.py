# from files import origen as aritmetica
import files.origen as aritmetica
from files.origen import *


p1 = Persona("Juan", 28)
print(p1)

resultado = aritmetica.sumar(3,4)
print(resultado)

resultado = aritmetica.multiplicar(3,4)
print(resultado)

p1 = Persona("Juan", 28)
print(p1)

# .................................................................................................................
from files.origen import Matematicas as mate

print(MI_CONSTANTE)
print(mate.PI)

MI_CONSTANTE = "Nuevo valor"
mate.PI = 3.14
print(MI_CONSTANTE)
print(mate.PI)

