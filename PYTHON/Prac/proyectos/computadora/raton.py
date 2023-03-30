class Raton:
    contador=0
    def __init__(self,tipo_entrada):
        Raton.contador+=1
        self.__id=Raton.contador
        self.__tipo_entrada=tipo_entrada
    def __str__(self):
        return 'ID RATON:'+str(self.__id)+'. TIPO DE ENTRADA:'+self.__tipo_entrada+ '\n'
