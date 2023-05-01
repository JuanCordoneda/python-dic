class Monitor:
    contador=0
    def __init__(self,marca,tamano):
        Monitor.contador+=1
        self.__id=Monitor.contador
        self.__marca=marca 
        self.__tamano=tamano

    def get_marca(self):
        return self.__marca
    def set_marca(self,marca):
        self.__marca=marca
    def get_tamano(self):
        return self.__tamano
    def set_tamano(self,tamano):
        self.__tamano=tamano

    
    def __str__(self):
        return 'ID MONITOR:'+str(self.__id)+'. MARCA:'+self.__marca+'. TAMAÑO:'+self.__tamano+'.\n'
