

'HERENCIA EN PYTHON'
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    def __str__(self):       #esta funcion se usa con el nombre del objeto solamente
        return "Nombre: " + self.nombre + ", edad: " + str(self.edad)    
    
class Empleado(Persona): #SUBCLASE, llama a la clase padre
    def __init__(self, nombre, edad, sueldo):
        super().__init__(nombre, edad)    #exporta los valores de la clase padre (nombre y edad)
        self.sueldo = sueldo            
        
    def __str__(self):
        return super().__str__() + ", sueldo: " + str(self.sueldo)      #exporta el str de la clase padre  
        
persona = Persona("Juan", 28)
print(persona)  

empleado = Empleado("Karla", 30, 500.00)
print(empleado)      

empleado.nombre = "Karla Ivone"
empleado.sueldo = 1000.00
print(empleado)


# ...................................................................................................................
'HERENCIA MÚLTIPLE'

class FiguraGeometrica:
    def __init__(self, ancho, alto):
        self.__ancho = ancho
        self.alto = alto
    def get_ancho(self):
        return self.__ancho
class Color:
    def __init__(self, color):
        self.color = color

class Cuadrado(FiguraGeometrica, Color):           #HERENCIA MULTIPLE
    def __init__(self,alto,ancho,color):
        FiguraGeometrica.__init__(self,alto,ancho)   #ALTERNATIVA AL SUPER, MAS CLARA, AGREGAR EL SELF
        #super().__init__(lado, lado)
        Color.__init__(self, color)
        
    def area(self):
        return 'el resultado es: ' + str(self.alto * FiguraGeometrica.get_ancho(self))   #ASI SE LLAMA A UNA CARIABLE ENCAPSULADA

cuadrado = Cuadrado(4,7, "rojo")
print(cuadrado.area())
print('el color es: ',cuadrado.color)

#Method Resolution Order
print(Cuadrado.mro())