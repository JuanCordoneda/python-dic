'ARMADOR DE PC'
facturas={}
a=False
b=False
print('ARMADOR DE PC')
resp=input('quieres añadir(a), o terminar: ')
if resp=='a':
    a=True
    b=False

else:
    print('programa terminado')
    print('facturas:',facturas)


while a:
    n=input('elemento: ')
    try:
        p=int(input('dime el valor: '))
        facturas.update({n:p})
        print('facturas:',facturas)
    except:
        resp=input('quieres añadir(a), o terminar: ')
        if resp=='a':
            b=False
            a=True
        else:
            print('programa terminado')
            print('facturas:',facturas)
            break

class PC:
    contador=0
    def __init__(self,lista):
        PC.contador+=1
        self.__id=PC.contador
        self.__lista=lista

    def get_precio(self):
        a=''
        for x in self.__lista:
            a+='Elemento:'+x+'. Valor: $'+str(self.__lista.get(x))+" | \n"
        return a

    def total(self):
        b=0
        for x in self.__lista:
            b+=self.__lista.get(x)
        return 'PRECIO TOTAL:'+str(b)
    
    def __str__(self):
        return 'ARMADOR DE PC:\n'+self.get_precio()+self.total()

pc=PC(facturas)
print(pc)       
 
# facturas={'micro ryzen 5 3400g': 20000, 'placa gtx 1650': 25000, 'mother asus 320': 7000, '2 teras ': 8000, '16 gb ram': 9000}



