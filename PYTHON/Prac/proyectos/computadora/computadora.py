from raton import Raton
from teclado import Teclado
from monitor import Monitor

class Computadora:
    contador=0  
    def __init__(self,nombre,monitor,teclado,raton):
        Computadora.contador+=1     
        self.__id=Computadora.contador
        self.__nombre=nombre    
        self.__monitor=monitor
        self.__teclado=teclado
        self.__raton=raton

    def get_nombre(self):
        return self.__nombre
    def set_nombre(self,nombre):
        self.__nombre=nombre
    def get_monitor(self):
        return self.__monitor
    def set_monitor(self,monitor):
        self.__monitor=monitor
    def get_teclado(self):
        return self.__teclado
    def set_teclado(self,teclado):
        self.__teclado=teclado
    def get_raton(self):
        return self.__raton
    def set_raton(self,raton):
        self.__raton=raton

    def __str__(self):
        # return 'COMPUTADORA ID:'+str(self.__id)+'. NOMBRE:'+self.__nombre+'\n'+str(self.__monitor)+str(self.__teclado)+str(self.__raton)
        return (
            f"""
            {self.__nombre}: {self.__id} 
                Monitor: {self.__monitor}
                Teclado: {self.__teclado} 
                Ratón: {self.__raton}
                """
        )

