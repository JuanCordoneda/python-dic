'EJ VIDEO 26'
class coche() :
    largoChasis=250
    anchochasis=120             #4propiedades
    ruedas=4
    enmarcha=False

    
    def arrancar(self):       #activador
        self.enmarcha=True  #es lo mismo que decir: micoche.enmarcha=True. Se abrevia poniendo micoche.arrancar()

    def estado(self):                                  #2 comportamientos
     if (self.enmarcha):                      
       return 'el auto esta prendido'                       
     else:
       return 'el auto esta parado'
micoche=coche()
micoche.arrancar()
print(micoche.estado())
print('ruedas del coche:',micoche.ruedas)

................................................................................................................


'EJ VIDEO 27'
class coche() :
    largoChasis=250
    anchochasis=120             #4propiedades
    ruedas=4
    enmarcha=False

    
    def arrancar(self):       #activador
        self.enmarcha=True  #es lo mismo que decir: micoche.enmarcha=True. Se abrevia poniendo micoche.arrancar()

    def estado(self):                                  #2 comportamientos
     if (self.enmarcha):                      
       return 'el auto esta prendido'                       
     else:
       return 'el auto esta parado'
print('...............................PRIMER OBJETO...................................')
micoche=coche()
micoche.arrancar()
print(micoche.estado())
print('ruedas del coche:',micoche.ruedas)
print('...............................SEGUNDO OBJETO..................................')
micoche2=coche()
# micoche2.arrancar()
print(micoche2.estado())
print('ruedas del coche:',micoche2.ruedas)
...............................................................................................................



'ej video 27. Parte 2'

class coche():
                                 #__init__ es un constructor. el que le da estado inicial a los objetos
    def __init__(self):       
     self.largoChasis=250
     self.anchochasis=120             #4propiedades. ESTADO INICIAL
     self.__ruedas=4   #__ haciendo eso, no va a ser accesible modificarlo desde el exterior de la clase.ENCAPSULAMIENTO
     self.enmarcha=False




    'activador. se agregan 2 parametros. micoche.arrancar(True or False)'
    'aca dice que self.enmarcha es igual al parametro[True, Flase] arrancamos.'
    def arrancar(self,ToF):       
        self.enmarcha=ToF         
        if(self.enmarcha):            #si es true
            return 'el coche esta en marcha'
        else:                          #si es false
            return'el coche esta parado'
    
    def estado(self):
        print ('el coche tiene', self.__ruedas, 'ruedas y un ancho de', self.anchochasis)


print('...............................PRIMER OBJETO...................................')
micoche=coche()  
print(micoche.arrancar(True)) #llama a la funcion arrancar. SI DEJAMOS EL () VACIO DARA ERROR.
print(micoche.estado())

print('...............................SEGUNDO OBJETO...................................')
micoche2=coche()
micoche2.anchochasis=100
micoche2.__ruedas=2    #no te deja modificar el valor de propiedad. POR EL __ (ENCAPSULADO)
print(micoche2.arrancar(False)) #llama a la funcion arrancar
micoche2.estado()     #como estado ya tiene un print. Para sacar el None hay q ponerlo sin print

# ............................................................................................................


'ej video 28'

class coche():
                                 #__init__ es un constructor. el que le da estado inicial a los objetos
    def __init__(self):       
     self.largoChasis=250
     self.anchochasis=120             #4propiedades. ESTADO INICIAL
     self.__ruedas=4   #__ haciendo eso, no va a ser accesible modificarlo desde el exterior de la clase.ENCAPSULAMIENTO
     self.enmarcha=False




    'activador. se agregan 2 parametros. micoche.arrancar(True or False)'
    'aca dice que self.enmarcha es igual al parametro[True, Flase] arrancamos.'
    def arrancar(self,ToF):       
        self.enmarcha=ToF       
        if(self.enmarcha):            #si el coche arranca, se llama a la funcion chequeo
          chequeo=self.__chequeo()      

        if(self.enmarcha and chequeo):            #si es true
            return 'el coche esta en marcha'

        elif (self.enmarcha and chequeo==False):
            return 'algo ha ido mal en el chequeo'

        else:                          #si es false
            return'el coche esta parado'
    
    def estado(self):
        print ('el coche tiene', self.__ruedas, 'ruedas y un ancho de', self.anchochasis)

    def __chequeo(self):   #Metodo encapsulado. Solo se puede usar dentro de la clase.
        print('realizando chequeo interno')                                 
        
        self.gasolina='OK'
        self.aceite='OK'
        self.puertas='cerradas'
        if (self.gasolina=='OK' and self.aceite=='OK' and self.puertas=='cerradas'):
            return True
        else:
            return False


print('...............................PRIMER OBJETO...................................')
micoche=coche()  
print(micoche.arrancar(True)) #llama a la funcion arrancar. SI DEJAMOS EL () VACIO DARA ERROR.
print(micoche.estado())

print('...............................SEGUNDO OBJETO...................................')
micoche2=coche()
micoche2.anchochasis=100
micoche2.__ruedas=2    #no te deja modificar el valor de propiedad. POR EL __ (ENCAPSULADO)
print(micoche2.arrancar(False)) #llama a la funcion arrancar
micoche2.estado()     #como estado ya tiene un print. Para sacar el NONE hay q ponerlo sin print
#micoche2.__chequeo()    #da error por estar encapsulado. Solo se  puede usar dentro de la clase
# ............................................................................................................

#ESTE CURSO SIGUE EN HERENCIA