class Productos:
    contador=0
    def __init__(self,marca,modelo,capacidad,precio):
        Productos.contador+=1
        self.__id=Productos.contador
        self.__marca=marca
        self.__modelo=modelo
        self.__precio=precio
        self.__capacidad=capacidad
    
    def get_precio(self):
        return self.__precio

    def __str__(self):
        return 'PRODUCTO ID:'+str(self.__id)+'. Marca:'+self.__marca+'. Modelo:'+self.__modelo+'. Capacidad:'+str(self.__capacidad)+ '. Precio:'+str(self.__precio)

class Orden:
    contador=0
    def __init__(self,productos):
        Orden.contador+=1
        self.__id=Orden.contador
        self.__productos=productos
    
    def precio_total(self):
        precio=0
        for x in self.__productos:
            precio+=x.get_precio()
        return 'EL PRECIO TOTAL DE LA ORDEN '+str(self.__id)+ ' ES:'+str(precio)

    def __str__(self):
        info=''
        for x in self.__productos:
            info+= x.__str__() + " | \n"
        return 'ORDEN ID:'+str(self.__id)+'. Productos: \n'+info+self.precio_total()



p1= Productos('Apple','Iphone 11 pro Max','128GB',100000)
p2= Productos('Apple','8 plus','64GB',50000)
p3= Productos('Samgung', 'J7','32GB', 20000)
p4= Productos('Samgung', 'J7','32GB', 20000)
total=[p1,p2,p3,p4]
totalb=[p1,p2,p3]
o1= Orden(total)
o2= Orden(totalb)

print(o1)
print(o2)
