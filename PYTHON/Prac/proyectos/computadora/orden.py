from raton import Raton
from teclado import Teclado
from monitor import Monitor
from computadora import Computadora

class Orden:
    contador=0
    def __init__(self,computadora):
        Orden.contador+=1
        self.__id=Orden.contador
        self.__computadora=computadora
    
    def agregar_computadora(self,computadora):
        self.__computadora.append(computadora)

    def __str__(self):
        strcompu=''
        for x in self.__computadora:
            strcompu+= x.__str__()
        return ( 
            f" ORDEN ID: {self.__id}."
            f"\nPRODUCTOS: \n {strcompu}"
            )
        
mon=Monitor('LG','22 PULGADAS')
rata=Raton('USB')
tecla=Teclado('USB')
compu1=Computadora('JUAN CRUZ',mon,tecla,rata)
compu2=Computadora('GAMER',mon,tecla,rata)
compu3=Computadora('ARMADA',mon,tecla,rata)
lista=[compu1,compu2]
o1=Orden(lista)
o1.agregar_computadora(compu3)
print(o1)



