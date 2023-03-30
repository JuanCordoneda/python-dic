from raton import Raton
from teclado import Teclado
from monitor import Monitor

class Disp_entrada:
    def __init__(self,raton,teclado,monitor):
        self.__raton=raton      
        self.__teclado=teclado
        self.__monitor=monitor

    def get_monitor(self):
        return self.__monitor
    def set_monitor(self,monitor):
        self.__monitor=monitor

    def get_raton(self):
        return self.__raton
    def set_raton(self,raton):
        self.__raton=raton

    def get_teclado(self):
        return self.__teclado
    def set_teclado(self,teclado):
        self.__teclado=teclado
    
    def __str__(self):
        return 'DISPOSITOVOS DE ENTRADA: \n'+str(self.__raton)+'.\n'+str(self.__teclado)+'. \n'+str(self.__monitor)

mon=Monitor('LG','22 PULGADAS')
rata=Raton()
tecla=Teclado()
disp=Disp_entrada(rata,tecla,mon)
print(disp)