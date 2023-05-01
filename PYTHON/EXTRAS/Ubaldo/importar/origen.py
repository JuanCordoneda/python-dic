def sumar(a, b):
    return a + b

def multiplicar(a, b):
    return a * b

class Persona:
    def __init__(self, nombre, edad):
        self.__nombre = nombre
        self.__edad = edad
        
    def __str__(self):
        return "Nombre: " + self.__nombre + ", edad: " + str(self.__edad) 

# ............................................................................................................
MI_CONSTANTE = "Valor de mi constante"

class Matematicas:
    PI = 3.1416