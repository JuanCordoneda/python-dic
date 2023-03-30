class Vehiculo:
    def __init__(self, color, marca, modelo):
        self.color= color
        self.__marca= marca
        self.modelo= modelo
    
    def __str__(self):             #esta funcion se usa con el nombre del objeto solamente
        return  ", marca: " + self.__marca + ", modelo:" + str(self.modelo) + ", de color: " + self.color 
    
    def __set_marca(self, marca):      #ESTA FUNCION MODIFICA LA VARIABLE ENCAPSULADA PERO ES PRIVADA
        self.__marca = marca   

    def auto_publico(self,marca):     #LLAMAR A LA FUNCION PRIVADA
        return self.__set_marca(marca)

class Coche(Vehiculo):
    def __init__(self,color,marca,modelo,vehiculo):
        super().__init__(color,marca,modelo)
        self.vehiculo= vehiculo
     
    def __str__(self):
        return 'vehículo: ' + self.vehiculo + super().__str__()

class Bicicleta(Vehiculo):
    def __init__(self,color,marca,modelo,vehiculo,frenos,estado):
        super().__init__(color,marca,modelo)
        self.vehiculo= vehiculo
        self.frenos= frenos
        self.estado= estado
     
    def __str__(self):
        return 'vehículo: ' + self.vehiculo + super().__str__() + ', frenos: '+ self.frenos +', estado: '+ self.estado

bici=Bicicleta('roja','GT',2012,'Bicicleta','normales','usada')
print(bici)
auto= Coche('gris','focus', 2014, 'coche')
print(auto)                             #llamando a la funcion
auto.color='rojo'
auto.auto_publico('jeep')
print(auto)

...................................................................................................................
'HERENCIA MULTIPLE'


class Figura:
    def __init__(self,largo,ancho):
        self.__largo=largo
        self.__ancho=ancho

    def get_ancho(self):
        return self.__ancho
    def set_ancho(self,ancho):
        self.__ancho=ancho

    def get_largo(self):
        return self.__largo
    def set_alto(self,largo):
        self.__largo=largo

    def __str__(self):
        return 'largo:'+str(self.__largo)+' ancho:'+str(self.__ancho)

class Color:
    def __init__(self,color):
        self.__color=color
    def get_color(self):
        return self.__color
    def set_color(self,color):
        self.__color=color
    def __str__(self):
        return 'el color es: '+self.__color

class Cuadrado(Figura,Color):
    def __init__(self,largo,ancho,color):
        Figura.__init__(self,largo,ancho)
        Color.__init__(self,color)

    def area(self): 
        
        return Figura.get_ancho(self)*Figura.get_largo(self)
    
    def __str__(self):
        return 'el color del cuadrado es: '+ Color.get_color(self)+ ' y el área es: '+ str(self.area())

class Rectangulo(Figura,Color):
    def __init__(self,largo,ancho,color):
        Figura.__init__(self,largo,ancho)
        Color.__init__(self,color)
    def area(self):
        return Figura.get_largo(self)*Figura.get_ancho(self)
    def __str__(self):
        return 'el color del rectángulo es: '+Color.get_color(self)+' y el area es: '+ str(self.area())

cuadrado=Cuadrado(5,6,"rojo")
print(cuadrado)

rectangulo=Rectangulo(7,10,'verde')
print(rectangulo)

............................................................................................
'HERENCIA Y CLASES ABSTRACTAS'
from abc import ABC, abstractmethod    #SE LLAMA LA LIBRERIA ABSTRACTA
class Telefono(ABC):
    def __init__(self,pantalla,pulgadas,modelo,marca):
        self.pantalla=pantalla
        self.pulgadas=pulgadas
        self.modelo=modelo
        self.marca=marca
        
    @abstractmethod
    def __str__(self):
        return 'marca: '+self.marca+'. modelo: '+self.modelo+'. pantalla: '+self.pantalla+'. pulgadas: '+self.pulgadas


class iphone(Telefono):
        def __init__(self,pantalla,pulgadas,modelo,marca,ios,color):
            Telefono.__init__(self,pantalla,pulgadas,modelo,marca)
            self.ios=ios
            self.color=color
        
        def __str__(self):
            return super().__str__()+'. color: '+self.color+'. ios: '+self.ios

class Usado(iphone):
    def __init__(self, pantalla, pulgadas, modelo, marca,ios,color,estado,years):
        iphone.__init__(self,pantalla,pulgadas,modelo,marca,ios,color)
        self.estado=estado
        self.years=years

    def __venta(self):
        return Telefono.__str__(self)+iphone.__str__(self)+'\nestado: '+self.estado+'. años:'+self.years


iphone=Usado('led','18,9','iphone 11 pro max','apple','13','negro','usado','3')
print(iphone)
