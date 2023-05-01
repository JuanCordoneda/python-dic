class Teclado:
    contador=0
    def __init__(self,tipo_entrada):
        Teclado.contador+=1
        self.__id=Teclado.contador
        self.__tipo_entrada=tipo_entrada
    def __str__(self):
        return 'ID TECLADO:'+str(self.__id)+'. TIPO ENTRADA: '+self.__tipo_entrada+ '\n'
