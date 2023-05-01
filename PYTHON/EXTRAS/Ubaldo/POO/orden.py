'CONTADOR DE PRODUCTOS'
class Producto: 
    contador=0        
    def __init__(self,nombre,precio):
        Producto.contador+=1           #sube el contador por cada obj creado
        self.__id = Producto.contador  #se le asigna ese número a la id
        self.__nombre= nombre          
        self.__precio= precio

    def get_precio(self):
        return self.__precio    #funcion que retorna el precio del producto

    def __str__(self):     #str del producto
        return 'ID:'+str(self.__id)+'. nombre:'+self.__nombre+ '. Precio:'+str(self.__precio)

class Orden:
    contador_ordenes = 0
    
    def __init__(self, productos):
        Orden.contador_ordenes += 1     #aumenta el contador
        self.__id_orden = Orden.contador_ordenes    #se le asigna el número de orden a la id
        self.__productos = productos  #lista de objetos de productos
    
    def agregar_producto(self, producto):   #funciona si se le agrega un objeto de producto
        self.__productos.append(producto)
    
    def calcular_total(self):
        total = 0    #contador
        for x in self.__productos:     # X recorre cada producto de la lista
            total += x.get_precio()    #se llama a la funcion de get_precio() de cada producto y se suman al total
        return 'precio total del producto: '+ str(total)+'\n'     #devuelve el precio final
        
    def __str__(self):
        cadena = ""                                   #string que encadena los productos de la orden
        for x in self.__productos:                    #recorre los elementos de la lista de productos ingresada 
            cadena += x.__str__() + " | \n"             #acá se llama al str de cada producto. por cada producto ingresado, se separa con un |            
        return "Orden: " + str(self.__id_orden) + ". Productos:\n" + cadena 

p1= Producto('pantalon',10000) 
p2= Producto('buzo',5000) 
p3= Producto('mancuerna', 20000)
p4= Producto('freezer',5000)
lista=[p1,p2,p3]   #se le agregan los elementos a la lista

o1=Orden(lista)  
print(o1)
print(o1.calcular_total())

o2=Orden(lista)
o2.agregar_producto(p4)    #se le suma un elem a la lista
print(o2)
print(o2.calcular_total())


     