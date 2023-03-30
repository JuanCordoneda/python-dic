class Persona:
    
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

#Modificar los valores
Persona.nombre = "Juan"
Persona.edad = 28

#Acceder a los valores
print(Persona.nombre)
print(Persona.edad)

#Creación de un objeto
persona1 = Persona("Karla", 30)
print(persona1.nombre)
print(persona1.edad)
print(id(persona1))
    
#Creación de un segundo objeto
persona2 = Persona("Carlos", 40)
print(persona2.nombre)
print(persona2.edad)    
print(id(persona2))

persona2.nombre= 'Juan'
print(persona2.nombre)

persona3= Persona('Marcos Muller',20)
print(persona3.edad)   
print(persona3.nombre)



# ..........................................................................................................
class Aritmetica:
    """Clase Artimetica para realizar las operaciones de sumar, restar, etc"""
    def __init__(self, operando1, operando2):
        self.operando1 = operando1
        self.operando2 = operando2
    
    def sumar(self):
        """Se realiza la operación con los atributos de la clase"""
        return self.operando1 + self.operando2   
    
    def restar(self):
        return self.operando1 - self.operando2   
    
    def multiplicar(self):
        return self.operando1 * self.operando2   
    
    def dividir(self):
        return self.operando1 / self.operando2   
             
    
#Creamos un nuevo objeto
aritmetica = Aritmetica(2, 4)  
print("Resultado sumar:", aritmetica.sumar())  
print("Resultado restar:", aritmetica.restar())  
print("Resultado multiplicar:", aritmetica.multiplicar())  
print("Resultado dividir:", aritmetica.dividir())  

#Creamos otro objeto
aritmetica2 = Aritmetica(3, 5)  
print("Resultado sumar:", aritmetica2.sumar())  
print("Resultado restar:", aritmetica2.restar())  
print("Resultado multiplicar:", aritmetica2.multiplicar())  
print("Resultado dividir:", aritmetica2.dividir())  
# ...................................................................................................................
'ENCAPSULAMIENTO DE VARIABLES'

class Persona:
    def __init__(self, nombre, edad):
        self.__nombre = nombre     #SE ENCAPSULA CON EL __
        self.__edad = edad
    def get_nombre(self):            #ESTA FUNCION MUESTRA LA VARIABLE NOMBRE ENCAPSULADA
        return self.__nombre
    def set_nombre(self, nombre):      #ESTA FUNCION MODIFICA LA VARIABLE ENCAPSULADA
        self.__nombre = nombre       
    def get_edad(self):                    #ESTA FUNCION MUESTRA LA VARIABLE EDAD ENCAPSULADA
        return self.__edad  
    def set_edad(self, edad):          #ESTA FUNCION MODIFICA LA VARIABLE ENCAPSULADA
        self.__edad = edad         
    def asistencia(self):
     return 'mi nombre es:',self.__nombre,'y tengo',self.__edad,'años.'

p1 = Persona("Juan", 18)
#print(p1.__nombre)  marca un error
print(p1.get_nombre())                      #MOSTRAR VARIABLE
print(p1.get_edad())
print(p1.asistencia())
#p1.__nombre = "Karla" marca un error
p1.set_nombre("Karla")                     #MODIFICAR VARIABLE
p1.set_edad(20)
print(p1.get_nombre())      
print(p1.get_edad())
print(p1.asistencia())

...................................................................................................................
'FUNCIONES PRIVADAS'
class Persona:
    def __init__(self, nombre, ape_materno):
        self.nombre = nombre 
        self.__apellido_materno = ape_materno 
    def __privado(self):                         #METODO PRIVADO
        print(self.nombre)
        print(self.__apellido_materno)
    def publico(self):                           #LLAMAR METODO PRIVADO
        self.__privado()

p1= Persona('JUAN','BOERI')
p1.publico()

...................................................................................................................
'CLASES ABSTRACTAS'
#ABC = Abstract Base Class
from abc import ABC, abstractmethod    #SE LLAMA LA LIBRERIA ABSTRACTA
class FiguraGeometrica(ABC):
    def __init__(self, ancho, alto):
        self.ancho = ancho
        self.alto = alto
       
    @abstractmethod          #SE LLLAMA AL MÉTODO ABSTRACTO
    def area(self):            #METODO ABSTRACTO
       pass

class Cuadrado(FiguraGeometrica):
    def __init__(self, ancho,alto):
        FiguraGeometrica.__init__(self, ancho, alto)

    def area(self):                          #LA CLASE HIJA ESTA OBLIGADA A LLAMAR AL METODO ASBTRACTO
        return self.alto * self.ancho

class Rectangulo(FiguraGeometrica):
    def __init__(self,ancho,alto):
        FiguraGeometrica.__init__(self, ancho, alto)
    def area(self):                          #LA CLASE HIJA ESTA OBLIGADA A LLAMAR AL METODO ASBTRACTO
        return self.alto * self.ancho

cuadrdado=Cuadrado(20,20)
print('area:',cuadrdado.area())

Rectangulo=Rectangulo(30,20)
print('area:',Rectangulo.area())

...................................................................................................................
'VARIABLES EN CLASES'
class MiClase:
    variable_clase = "1"    #no es necesario crear un objeto para llamarla
    
    def __init__(self, variable_instancia):
        self.variable_instancia = variable_instancia  #si es necesario
        
print(MiClase.variable_clase)  
MiClase.variable_clase = "2"
print(MiClase.variable_clase)  

print('....................................')

objeto1 = MiClase("a") 
print(objeto1.variable_instancia) 
print(objeto1.variable_clase)       #esta clase ha sido modificada
print('....................................')

MiClase.variable_instancia = "b"
print(MiClase.variable_instancia) #se modifica la variable 
print(objeto1.variable_instancia)  #no se mofica la variable ya que es un objeto creado

print('....................................')

.............................................................................................................
'METODOS  DE  CLASE'
class MiClase:
    
    variable_clase = "Variable clase"
    
    def __init__(self):
        self.variable_instancia = "Variable instancia"
    
    @staticmethod
    def metodo_estatico():
        print("Método estático")
        print(MiClase.variable_clase)
        #Desde un método estático no podemos acceder a una variable de instancia (__INIT__)
        #print(MiClase.variable_instancia) #ERROR
        
    def metodo_instancia(self):
        self.metodo_estatico()
        self.metodo_clase()
        print(self.variable_clase)
        print(self.variable_instancia)
            
        
MiClase.metodo_estatico()       
MiClase.metodo_clase() 

print()
objeto1 = MiClase()
objeto1.metodo_instancia()


.............................................................................................................
'CONTADOR DE OBJETOS'
class Producto: 
    contador=0
    def __init__(self,nombre,precio):
        Producto.contador+=1
        self.__id = Producto.contador
        self.__nombre= nombre
        self.__precio= precio

    def __str__(self):
        return 'id:'+str(self.__id)+'. nombre:'+self.__nombre+ '. Precio:'+str(self.__precio)

p1=Producto('motomel',110000)
print(p1)
p2=Producto('yamaha',200000)
print(p2)


.............................................................................................................
'POLIMORFISMO'
class coche():
    def __str__(self):
        return 'me desplazo utilizando 4 ruedas'
class moto():
    def __str__(self):
        return 'me desplazo utilizando 2 ruedas'
class camion():
    def __str__(self):
        return 'me desplazo utilizando 6 ruedas'


'con polimorfismo'
def desplazamientovehiculo(vehiculo):     #vehiculo tiene q tener el lugar de la cosa q queremos llamar
    print(vehiculo)            #aqui llamamos a la funcion de STR

miauto=coche()
desplazamientovehiculo(miauto)    