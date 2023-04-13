# -------------------------------------------------- IMPORTAR ---------------------------------------------------------
# import files.origen as aritmetica
# from files.origen import *
import modulo1
print(modulo1.data)
modulo1.ejecutar() #ejecuta metodo
if __name__ == '__main__':
  print('IMPRIME AL EJECUTARSE EL ARCHIVO ')
# ---------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------- PRINT ------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------
name='JUAN CRUZ'
last_name='CORDONEDA'
template = "Hola, mi nombre es " + name + " y mi apellido es " + last_name
template = "Hola, mi nombre es {} y mi apellido es {}".format(name, last_name)
template = f"Hola, mi nombre es {name} y mi apellido es {last_name}"
# ---------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------- VARIABLES --------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------
nombre = 'juan'
print(type(nombre))                   # muestra el tipo de variable
apellido = input('dime tu nombre: ')  # input para el usuario
apellido = int(apellido)              # modifiar el tipo de variable
# ---------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------- VARIABLES STRING ----------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------
MI_CONSTANTE = "Valor de mi constante"
inverted = nombre[::-1]               # invierte las palabras
extraer = nombre[1:8]                 # recorta las palabras
nombre.capitalize()                   # pone la primera en mayúscula
nombre.upper()                        # pone todo en mayusculas
nombre.lower()                        # cambia a minusculas
nombre.swapcase()                     # cambia mayus a minus y al revez
nombre.title()                        # pone todo en mayusculas
nombre.count("a")                     # contar cuantas veces aparece una cadena de caracteres
nombre.find('hola')                   # encontrar la posicion en donde aparece un caracter en un texto
nombre.rfind()                        # hace lo mismo con find, pero este lo hace contando desde atras
nombre.isdigit()                      # si es un numero devuelve true
nombre.isalum()                       # comprobar si son alfanumericos
nombre.isalpha()                      # comprobar si hay solo letras
nombre.startswith('Ella')             # comprobar si el string empieza con...
nombre.startswith('Rust')             # comprobar si el string termina con...
nombre.split()                        # separa x palabras utilizando espacios
nombre.strip()                        # borrar espacios sobrantes al pcipo y al final
nombre.replace('Python', 'Go')        # cambia letra o palabra x otra dentro de un string
nombre.partition('i')                 # particiona, devuelve=('jav', 'i', 'er') 
# ---------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------- VARIBALES INTEGER ---------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------
round(0.8888,2)                       # REDONDEAR: 2 es el número de números atras de la coma
my_iter = iter(range(1, 4))
print(next(my_iter))#1
print(next(my_iter))#2
print(next(my_iter))#3
# ---------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------- ARRAY ------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------
lista=[1, 2, 3, 4, 5]
rango = list( range(10) )             #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
lista=lista.sort()                    # ORDENAR ELEMENTOS DEL ARRAY
lista=lista.sort(reverse=True)        # ORDENAR ELEMENTOS DEL ARRAY (INVERTIDOS)
lista=lista.reverse()                 # ORDENAR ELEMENTOS DEL ARRAY INVERTIDO
index=lista.index('todo 2')           # obtiene la posicion del elemento
lista=lista.append(10)                # agregar un elemento
lista=lista.insert(0,10)              # agregar un elemento en pos 0.
lista=lista.extend([11,12])           # agregar un array al array
lista= lista + ['i','j','k']          # agregar un array al array otra forma
lista[-1] = 10                        # agregar al array de otra froma al final
lista.remove('todo 1')                # quitar elem de un array
lista= lista.pop(2)                   # quitar elem de un array
lista= lista.pop()                    # quitar el ultimo elemento
contador=len(lista)                   # largo del array
suma=sum(lista)                       # SUMA TODOS LOS VALORES DEL ARRAY
print(lista[:3])                      # imprime todos los 0,1,2
my_list = list('tupla')               # convertir tupla en lista

#array bidimensional
people = [{'name': 'nico','age': 34},{'name': 'zule','age': 45},{'name': 'santi','age': 4}]
print(list(zip(['nico', 'zule', 'santi'], [12, 56, 98]))) #UNIR 2 ARRAY EN 1 ARRAY

#MAP
print(list(map(lambda i: i * 2, [1, 2, 3, 4])))    #[2, 4, 6, 8]
print(list(map(lambda x, y: x + y, [1, 2, 3, 4], [5, 6, 7]))) # [6, 8, 10]

#FILTER
new_numbers = list(filter(lambda x: x % 2 == 0, [1,2,3,4,5])) #ARRAY CON NUMEROS PARES
new_list = list(filter(lambda item: item['name'] == 'nico', people)) #ARRAY QUE TENGA 'nico' como nombre

# RECORRER ARRAY
for i in lista:                       
    print(i*'+')
for person in people:
    print('name =>', person['name'])

numbers_v2 = [element * 2 for element in range(1, 11)]  #for dentro de array: [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
numbers_v2 = [i * 2 for i in range(1, 11) if i % 2 == 0] #for dentro de array: [4, 8, 12, 16, 20]
# ---------------------------------------------------------------------------------------------------------------------
# -------------------------------------------- DICCIONARIOS -----------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------
diccionario = {                                       #un diccionario está compuesto de llave,valor (key,value)               
    "IDE": "ELEMENTO 1",
    'langs': ['python', 'javascript'],
    'age': 99
}    
print(diccionario.items())                            #var_dump
print(diccionario.items())                            #primer elem
print(diccionario.values())                           #segundo elem
diccionario["PK"] = "Primary Key"                     #agregar nuevos elementos
diccionario.update({'a':10,'b':40})                   #agregar nuevos elementos de otra forma
diccionario['langs'].append('php')                    #agregar a lista
variable= diccionario["IDE"]                          #accediendo a un elemento
variable= diccionario.get("IDE")                      #accediendo a un elemento, mismo resultado
diccionario.get('Sex', "respuesta equivocada")        #accediendo a un elemento, Si no lo encuentra, tira excepcion
diccionario["IDE"]= "ELEMENTO"                        #modificando valores
variable= "IDE" in diccionario                        #comprobando existencia de un elemento
del diccionario['last_name']                          #remover elementos
diccionario.pop("DBMS")                               #remover elementos
diccionario.clear()                                   #limpiar 
variable=len(diccionario)                             #largo
print('avion' in diccionario)                         #false

for nombre in diccionario:
  print(nombre + " tiene " + str(diccionario[nombre]) + "años.")
for key, value in diccionario.items():
  print(key, '=>', value)

new_dict = {name: age for (name, age) in zip(['nico', 'zule', 'santi'], [12, 56, 98])} #UNIR 2 ARRAYS EN 1 DICCIONARIO
population_v2 = { country: random.randint(1, 100)  for country in ['col', 'mex', 'bol', 'pe']} #CREAR DICCIONARIO {'col': 47, 'mex': 64, 'bol': 66, 'pe': 17}

#MAP
items = [{'product': 'camisa','price': 100,},{'product': 'pantalones','price': 300},{'product': 'pantalones 2','price': 200}]
print(list(map(lambda item: item['price'], items))) #ITERA Y SACA LOS PRECIOS:[100, 300, 200]

def add_taxes(item):
  item['taxes'] = item['price'] * .19 #MODIFICA VALORES
  return item
print(list(map(add_taxes, items))) #[{'product': 'camisa', 'price': 100, 'taxes': 19.0}, {'product': 'pantalones', 'price': 300, 'taxes': 57.0}, {'product': 'pantalones 2', 'price': 200, 'taxes': 38.0}]
# ---------------------------------------------------------------------------------------------------------------------
# -------------------------------------------- {SET O CONJUNTOS} ------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------
conju = {'col', 'mex', 'bol'}                    # conjunto (no se repite y se ordena) 
conju = set([1,2,3,4,5,6])                       # {1, 2, 3, 4} 
conju = set('hoola')                             # {'h', 'o', 'a', 'l'}
conju = {1, 'hola', False, 12.12}                # puede ser mixto. El set se ordena solo, lo importante es lo que tengo dentro.
conju = set(('abc','cbv','as','abc'))            # {'as', 'abc', 'cbv'}
size = len(conju)                                # obtener el largo
size.add('arg')                                  # agregar 
conju.update({'ar', 'ecua', 'pe'})               # agregar muchos
conju = conju.union('conju2')                    # unir 2 conjus
conju = conju | 'conju2'                         # unir 2 conjus
set_c = conju.intersection('conju2')             # interseccionar las igualdades
print(conju & 'conju2')                          # interseccionar las igualdades
set_c = conju.difference('conju2')               # interseccionar las diferencias (muestra elementos que no coinciden de conju1)
print(conju - 'conju2')                          # interseccionar las diferencias (muestra elementos que no coinciden de conju1)
set_c = conju.symmetric_difference('conju2')     # interseccionar las diferencias (muestra elementos que no coinciden de las 2 conjus)
print(conju ^ 'conju2')                          # interseccionar las diferencias (muestra elementos que no coinciden de las 2 conjus)
conju.remove('col')                              # eliminar
conju.discard('arg')                             # eliminar
conju.clear()                                    # vaciar

print('col' in conju)                            # true
edades = {'juanjo': 35, 'pedro': 45, 'valeria': 24}   #for
for nombre in edades:
  print(nombre + " tiene " + str(edades[nombre]) + "años.")
# ---------------------------------------------------------------------------------------------------------------------
# -------------------------------------------- (TUPLAS) ---------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------
planetas = ("Marte", "Júpiter", "Venus")         #Estructura de datos inmutables que contiene una secuencia ordenada de elementos los elementos no se pueden modificar, pero si agregar nuevos o eliminar
numeros = (1, 2, 3, 4)                           
a=tuple([1,2,3,4,5,6])                           #convertir en una tupla
print(len(planetas))                             #longitud
print( "Marte" in planetas)                      #revisar si un elemento está presente
planetas.add("Tierra")                           #agregar
planetas=planetas.union({2,4,6,7,2})             #unir 2 tuplas y ordenarlas
planetas.discard("Júpiters")                     #eliminar
planetas.clear()                                 #limpiar el set
del planetas                                     #eliminar el set
print(numeros&numeros)                           #muestra las intercepciones
print(numeros|numeros)                           #une las 2 tuplas
print(numeros-numeros)                           #resta las 2 tuplas
for element in planetas:                         #recorrer tupla
  print(element)
# ---------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------- CODICIONES -------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------
numero = 0
if numero > 1:
    print('ganaste')
elif not (numero == 1):
    print('el número NO es 1')
else:
    print('else')
# IF REDUCIDO
print("Condicion verdadera") if numero > 1 else print("Condicion falsa") 
# ---------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------- WHILE ------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------
materias = {'lógica': 6, 'matematica': 8, 'sisop': 7}
materia = input('dime la materia: ')
# while True:
# while counter < 10: 
while materia:
    nota = materias.get(materia)
    if nota:
        print('tu nota es: ', nota)
    else:
        print('aun no se rindio')
    materia = input('dime la materia: ')
else:
    print('FIN DE SICLO')
# ---------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------- FOR --------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------
#array
my_list = [23, 45, 67, 89 ,43]                          
for element in my_list:
  print(element)

#array bidimensional
people = [{'name': 'nico','age': 34},{'name': 'zule','age': 45},{'name': 'santi','age': 4}]
for person in people:
  print('name =>', person['name'])

#matrices
matriz = [[1,2,3],[4,5,6],[7,8,9]]
for row in matriz:
  print(row)
  for column in row:
    print(column)

numbers_v2 = [element * 2 for element in range(1, 11)]  #for dentro de array: [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
numbers_v2 = [i * 2 for i in range(1, 11) if i % 2 == 0] #for dentro de array: [4, 8, 12, 16, 20]

#tuplas
my_tuple = ('nico', 'juli', 'santi')
for element in my_tuple:
  print(element)

#diccionarios 
product = {
  'name': 'Camisa',
  'price': 100,
  'stock': 89
}
for key in product:
  print(key, '=>', product[key])
for key, value in product.items():
  print(key, '=>', value)

#string
contador = 0
nombre = 'Pedro'
for i in nombre:
    if i == 'o':
        continue                                     #PASA A LA SGTE EJECUCION
    contador += 1
    print(i)
print(contador)

# for x in range(5,50,5): pcipio, final, numero de pasos
for x in range(1000):
    if x % 13 != 0:
        continue                                     #PASA A LA SGTE EJECUCION
    print(x, x ** 2)


for i in range(10,0,-1):                            #rangos entre 10,1
    print(i)

my_iter = iter(range(1, 4))
print(next(my_iter))#1
print(next(my_iter))#2
print(next(my_iter))#3
# ---------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------- FUNCIONES --------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------
def cualquiera(a, b, c, d=10, e=20):
   return a, b*c, d + e
result, width, text = cualquiera(1,2,3)

def tupla(*a):
    print(a)
tupla(1,2,3,5,6,7,8)              #GENERADOR DE TUPLAS

def diccionario(**b):
    print(b)
diccionario(a=10,b=20)           #GENERADOR DE DICCIONARIOS

def d(*a,**b):
    print(a,b)
d(1,'hola',3,4,a=20,b=30)          #MEZCLADOS

#PARAMETROS EN FUNCIONES
def increment(x):
  return x + 1
def high_ord_func(x, func):
  return x + func(x)
print(high_ord_func(2, increment))        # 2 + (2 + 1)
# ---------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------- FUNCIONES LAMBDA -------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------
#EJ 1
increment_v2 = lambda x: x + 1          #PRIMER ELEMENTO PARAMETRO
print(increment_v2(20)) #21
#EJ 2
full_name = lambda name, last_name: f'Full name is {name.title()} {last_name.title()}'
print(full_name('nicolas', 'perez casas')) #Full name is Nicolas Perez Casas
#FUNCIONES CON FUNCION COMO PARAMETRO
high_ord_func_v2 = lambda x, func: x + func(x) 
print(high_ord_func_v2(2, lambda x: x +1))  #5  (2+(2+1))
print(high_ord_func_v2(2, lambda x: x + 2)) #6  (2+(2+2))
print(high_ord_func_v2(2, lambda x: x * 5)) #12 (2+(2*5))

#ARRAY MAP
print(list(map(lambda i: i * 2, [1, 2, 3, 4])))    #[2, 4, 6, 8]
print(list(map(lambda x, y: x + y, [1, 2, 3, 4], [5, 6, 7]))) # [6, 8, 10]
#ARRAY FILTER
new_numbers = list(filter(lambda x: x % 2 == 0, [1,2,3,4,5])) #ARRAY CON NUMEROS PARES
new_list = list(filter(lambda item: item['name'] == 'nico', people)) #ARRAY QUE TENGA 'nico' como nombre

#DICCIONARIOS
items = [{'product': 'camisa','price': 100,},{'product': 'pantalones','price': 300},{'product': 'pantalones 2','price': 200}]
print(list(map(lambda item: item['price'], items))) #ITERA Y SACA LOS PRECIOS:[100, 300, 200]
# ---------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------- EXCEPCIONES ------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------
try:
    print('try') 
except ZeroDivisionError as error:
  print(error)
except AssertionError as error:
  print(error)
except Exception as error:
  print(error)
finally:                                             #el finally se ejecuta SIEMPRE
    print('finally')    
    # exit()

age = 10
if age < 18:
  raise Exception('No se permiten menores de edad') #lanza una excepcion

assert 2+2 == 5 #da error

Exception                   #Clase base para todas las excepciones
SystemError                 #Se genera cuando se produce un error del sistema
TypeError                   #Se genera cuando se combinan dos tipos diferentes
ArithmeticError             #Se genera cuando se produce un error en los cálculos numéricos
AssertionError              #Se genera cuando falla una declaración de afirmación
AttributeError              #Se genera cuando falla la asignación o la referencia de atributo
EOFError                    #Se genera cuando el método input() alcanza una condición de “fin de archivo” (EOF)
FloatingPointError          #Se genera cuando falla un cálculo de punto flotante
GeneratorExit               #Se genera cuando se cierra un generador (con el método close())
ImportError                 #Se genera cuando no existe un módulo importado
IndentationError            #Se genera cuando la sangría no es correcta
IndexError                  #Se genera cuando no existe un índice de una secuencia
KeyError                    #Se genera cuando una clave no existe en un diccionario
KeyboardInterrupt           #Se genera cuando el usuario presiona Ctrl+c, Ctrl+z o Eliminar
LookupError                 #Se genera cuando no se pueden encontrar los errores generados
MemoryError                 #Se genera cuando un programa se queda sin memoria
NameError                   #Se genera cuando una variable no existe
NotImplementedError         #Se genera cuando un método abstracto requiere una clase heredada para anular el método
OSError                     #Se genera cuando una operación relacionada con el sistema provoca un error
OverflowError               #Se genera cuando el resultado de un cálculo numérico es demasiado grande
ReferenceError              #Se genera cuando no existe un objeto de referencia débil
RuntimeError                #Se genera cuando ocurre un error que no pertenece a ninguna expectativa específica
StopIteration               #Se genera cuando el método next() de un iterador no tiene más valores
SyntaxError                 #Se genera cuando se produce un error de sintaxis
TabError                    #Se genera cuando la sangría consta de tabulaciones o espacios
SystemExit                  #Se genera cuando se llama a la función sys.exit()
UnboundLocalError           #Se genera cuando se hace referencia a una variable local antes de la asignación
UnicodeError                #Se genera cuando se produce un problema Unicode
UnicodeEncodeError          #Se genera cuando se produce un problema de codificación Unicode
UnicodeDecodeError          #Se genera cuando se produce un problema de decodificación Unicode
UnicodeTranslateError       #Se genera cuando se produce un problema de traducción Unicode
ValueError                  #Se genera cuando hay un valor incorrecto en un tipo de datos especificado
ZeroDivisionError           #Se genera cuando el segundo operador en una división es cero
# ---------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------- POO --------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------
class Persona:
    variable_clase = "1"    #no es necesario crear un objeto para llamarla
    
    def __init__(self, nombre, edad): #constructor
        self.nombre = nombre
        self.__edad = edad            #SE ENCAPSULA CON EL __

    def mostrar(self):                #Se realiza la operación con los atributos de la clase
        return self.nombre + ', edad: ' +  self.__edad   

    def get_edad(self):               #GET
        return self.__edad  
    def set_edad(self, edad):         #SET
        self.__edad = edad     

    def __privado(self):                         #METODO PRIVADO
        print(self.nombre)
        print(self.__apellido_materno)
    def publico(self):                           #LLAMAR METODO PRIVADO
        self.__privado()

    @staticmethod
    def metodo_estatico(): #Desde un método estático no podemos acceder a una variable de instancia (__INIT__)
        print("Método estático")
        print(Persona.variable_clase)
        print(Persona.variable_instancia) #ERROR

persona1 = Persona("Karla", 30) #Creación de un objeto
persona1.nombre= 'Juan'         #modificar atributo de un objeto
print(persona1.nombre)          #Acceder a los valores
persona1.set_edad(20)           #GET
print(persona1.get_edad())      #SET
print(persona1.mostrar())       #acceder a metodos
print(id(persona1))             #acceder a id
# ---------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------- HERENCIA ---------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    def __str__(self):       #esta funcion se usa con el nombre del objeto solamente
        return "Nombre: " + self.nombre + ", edad: " + str(self.edad)    
    
class Empleado(Persona): #SUBCLASE, llama a la clase padre
    def __init__(self, nombre, edad, sueldo):
        super().__init__(nombre, edad)    #exporta los valores de la clase padre (nombre y edad)
        self.sueldo = sueldo            
        
    def __str__(self):
        return super().__str__() + ", sueldo: " + str(self.sueldo)      #exporta el str de la clase padre  
        
persona = Persona("Juan", 28)
print(persona)  

empleado = Empleado("Karla", 30, 500.00)
print(empleado)      

empleado.nombre = "Karla Ivone"
empleado.sueldo = 1000.00
print(empleado)
# -----------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------- HERENCIA MÚLTIPLE --------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------------
class FiguraGeometrica:
    def __init__(self, ancho, alto):
        self.__ancho = ancho
        self.alto = alto
    def get_ancho(self):
        return self.__ancho
    
class Color:
    def __init__(self, color):
        self.color = color

class Cuadrado(FiguraGeometrica, Color):           #HERENCIA MULTIPLE
    def __init__(self,alto,ancho,color):
        FiguraGeometrica.__init__(self,alto,ancho)   #ALTERNATIVA AL SUPER, MAS CLARA, AGREGAR EL SELF
        #super().__init__(lado, lado)
        Color.__init__(self, color)
        
    def area(self):
        return 'el resultado es: ' + str(self.alto * FiguraGeometrica.get_ancho(self))   #ASI SE LLAMA A UNA CARIABLE ENCAPSULADA

cuadrado = Cuadrado(4,7, "rojo")
print(cuadrado.area())
print('el color es: ',cuadrado.color)
#Method Resolution Order
print(Cuadrado.mro())
# ---------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------- POLIMORFISMO -----------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------
class coche():
    def __str__(self):
        return 'me desplazo utilizando 4 ruedas'
class moto():
    def __str__(self):
        return 'me desplazo utilizando 2 ruedas'
class camion():
    def __str__(self):
        return 'me desplazo utilizando 6 ruedas'


'con polimorfismo'
def desplazamientovehiculo(vehiculo):     #vehiculo tiene q tener el lugar de la cosa q queremos llamar
    print(vehiculo)            #aqui llamamos a la funcion de STR

miauto=coche()
desplazamientovehiculo(miauto)    
# -----------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------- CLASES ABSTRACTAS --------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------------
#ABC = Abstract Base Class
from abc import ABC, abstractmethod    #SE LLAMA LA LIBRERIA ABSTRACTA
class FiguraGeometrica(ABC):
    def __init__(self, ancho, alto):
        self.ancho = ancho
        self.alto = alto
       
    @abstractmethod          #SE LLLAMA AL MÉTODO ABSTRACTO
    def area(self):            #METODO ABSTRACTO
       pass

Rectangulo=FiguraGeometrica(30,20)
print('area:',Rectangulo.area())
# ---------------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------- SQL -----------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------------
import psycopg2

conexion = psycopg2.connect(user='postgres',
                 password='admin',
                 host='127.0.0.1',
                 port='5432',
                 database='test_db')                #nombre de la database

cursor = conexion.cursor()                                     #este comando 'cursor' te deja leer datos de una base de datos. es el permiso
sentencia = 'SELECT * FROM persona'                            
cursor.execute(sentencia)                                      #el cursor ejecuta la sentencia
registros = cursor.fetchall()                                  #fetchall hace que se muestre toda la info del comando
registros = cursor.fetchone()                       #esta funcion solo va a regresar UN REGISTRO por fetchONE

print(registros)                                               #se imprime fetchall para ver el registro 

cursor.close()
conexion.close()
# ----------------------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------- SQL (INSERT / UPDATE / DELETE)-------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------------------
cursor = conexion.cursor()
# ###############EJEMPLO INDIVIDUAL#######################
sentencia = 'INSERT INTO persona(nombre, apellido, apodo) VALUES(%s, %s, %s)'
valores = ('Carlos','Lara','pupe')
cursor.execute(sentencia, valores)
# ###############EJEMPLO GRUPAL#######################
sentencia = 'INSERT INTO persona(nombre, apellido, apodo) VALUES(%s, %s, %s)'
valores = (
    ('Marcos','Cantu','cantux'),
    ('Angel','Quintana','quini'),
    ('Marcos','Gonzalez','gordo')              #HAY QUE HACER UNA TUPLA CON TODOS LOS REGISTROS A MODIFICAR
)
cursor.executemany(sentencia, valores)                #EXECUTEMANY
# ###############EJEMPLO UPDATE#######################
sentencia = 'UPDATE persona SET nombre = %s, apellido = %s, apodo = %s WHERE id_persona = %s'
valores = (
    ('Juan', 'Perez', 'jperez@mail.com', 7),
    ('Karla1', 'Gomez2', 'kgomez3@mail.com', 8)              #HAY QUE HACER UNA TUPLA CON TODOS LOS REGISTROS A MODIFICAR
)
cursor.executemany(sentencia, valores)                       #EXECUTEMANY
# ###############EJEMPLO DELETE#######################
sentencia = 'DELETE FROM persona WHERE id_persona = %s'
entrada = input("Proporciona la pk a eliminar: ")
valores = (entrada,)
cursor.execute(sentencia, valores)
# ###############EJEMPLO DELETE MULTIPLE#######################
cursor = conexion.cursor()
sentencia = 'DELETE FROM persona WHERE id_persona = %s'
valores = (
    ('7'),('6')
)
cursor.executemany(sentencia, valores)
#####################################################

try:
    cursor.executemany(sentencia, valores)
    conexion.commit()       #guardamos la información en la base de datos
    registros_insertados = cursor.rowcount     #CON ESTE COMANDO PODEMOS VER LA CANTIDAD DE REGISTROS QUE SE INSERTARON
    print(f'Registros insertados: {registros_insertados}')
except Exception as e:                                     #CATCH EXCEPTION
    conexion.rollback()                                    #rollback da marcha atras a todas las operaciones pendientes
    print(f'Ocurrió un error en la transacción: {e}')
finally:
    cursor.close()
    conexion.close()
# ---------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------- RECORRER SELECT --------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------
sentencia = 'SELECT * FROM persona WHERE id_persona IN %s'                   
entrada = input("Proporciona las pk a buscar (separado por comas): ")       
tupla = tuple(entrada.split(','))                                           #creador de tupla
print(tupla)
llaves_primarias = (tupla,)                                      #meter la tupla dentro de otra tupla
cursor.execute(sentencia, llaves_primarias)                        #ejecutar la sentencia y la tupla de tuplas
registros = cursor.fetchall()                                    #imprimir TODOS los registros (fetchall)
print(registros)
# for registro in registros:
#     print(registro)

cursor.close()
conexion.close()
# ---------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------- REQUESTS ---------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------
import requests #pip3 install requests

def get_categories():
    r = requests.get('https://api.escuelajs.co/api/v1/categories') #busca la request
    print(r.status_code) #estado
    print(r.text)  #muestra todo el texto
    print(type(r.text)) # muestra el formato
    categories = r.json() #lo convierte en un json
    for category in categories:
        print(category['name'])
# ---------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------- FECHAS -----------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------
from datetime import *                               # IMPORTA FECHA
hoy = date.today()                                   # dia actual
fecha = datetime.strptime('6/10/1999', "%d/%m/%Y")   # convertir fecha en objeto
año=fecha.year
mes=fecha.month
dia=fecha.day
hora = time(12,00)                                   #son las 12.00
hoy= date.today().strftime('%d,%m,%y')               #hora actual

# SEGUNDA OPCION
import time
local = time.localtime()
result = time.asctime(local)
print(result) #FECHA ACTUAL
# ---------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------- ARCHIVOS ---------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------
#https://platzi.com/clases/4260-python-funciones/55086-escribir-en-un-archivo/
try:
    archivoleer=open("prueba.txt",'r')          #leer abrir (READ)
    archivoagregar = open("prueba.txt", "a")    #escribir (APPEND)
    archivosobre = open("prueba.txt", "w")      #sobreescribir (WRITE)

    print(archivoleer.read())                   #leer
    print(archivoleer.read(5))                  #la funcion me va a leeer solo 5 caracteres
    print(archivoleer.readline())               #lee solo la primer línea, mientras mas lo pones mas lee
    print(archivoleer.readlines())              #crea una lista con cada línea de nuestro archivo
    archivoagregar.write("Agregamos info\n")           #ESTE METODO SOBREESCRIBE ARCHIVOS
    archivoagregar.remove('ruta_archivo.txt')          #ELIMINAR ARCHIVOS
    archivosobre.write("Agregamos info al archivo\n")  #ESTE METODO AGREGA TEXTO
except Exception as e:     
    print('ocurrió un error',e) 
finally:
    archivosobre.close() #después de close ya no podemos trabajar con el archivo

#EJEMPLO 1
file = open('./ruta_archivo.txt')
print(file.read())
print(file.readline())
print(file.readline())
print(file.readline())
print(file.readline())
file.close()
#EJEMPLO 2
with open('./text.txt') as file:
  for line in file:
    print(line)
# ---------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------- LEER CSV ---------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------
#https://platzi.com/clases/4260-python-funciones/55087-leer-un-csv/
import csv
def read_csv(path):
  with open(path, 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    header = next(reader)
    data = []
    for row in reader:
      iterable = zip(header, row)
      country_dict = {key: value for key, value in iterable}
      data.append(country_dict)
    return data

if __name__ == '__main__':
  data = read_csv('./app/data.csv')
  print(data[0])
# ---------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------- GRAFICAS ---------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------
#https://platzi.com/clases/4260-python-funciones/55088-creando-una-grafica/
import matplotlib.pyplot as plt

def generate_bar_chart(labels, values):
  fig, ax = plt.subplots()
  ax.bar(labels, values)
  plt.show()

def generate_pie_chart(labels, values):
  fig, ax = plt.subplots()
  ax.pie(values, labels=labels)
  ax.axis('equal')
  plt.show()

if __name__ == '__main__':
  labels = ['a', 'b', 'c']
  values = [10, 40, 800]
  # generate_bar_chart(labels, values)
  generate_pie_chart(labels, values)
# ---------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------- MODULOS ----------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------
import random
random.randint(1,100)
options = ('piedra', 'papel', 'tijera')
computer_option = random.choice(options)
population_v2 = { country: random.randint(1, 100)  for country in ['col', 'mex', 'bol', 'pe']} #CREAR DICCIONARIO {'col': 47, 'mex': 64, 'bol': 66, 'pe': 17}

#MUESTRA LA RUTA
import sys 
print(sys.path) 

#EXPRESIONES REGULARES
import re
text = 'Mi numero de telefono es 311 123 121, el codigo del pais es 57, mi numero de la suerte 3'
result = re.findall('[0-9]+', text) #EJECUTA EXPRESION
print(result)

#TIEMPO
import time
local = time.localtime()
result = time.asctime(local)
print(result) #FECHA ACTUAL

#MANEJADOR DE LISTAS
import collections
numbers = [1,1,2,1,2,1,4,5,3,3,21]
counter = collections.Counter(numbers) #FRECUENCIA DE NUMEROS EN LA LISTA {1: 4, 2: 2, 3: 2, 4: 1, 5: 1, 21: 1}
print(counter)
# ---------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------- PIP ----------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------
# PIP es el gestor de paquetes de python, es posible buscar librerías en la pagina pypi.org.

# Ver la versión de pip pip3 -v.
# Instalación de paquetes pip3 install <libreria>.
# Listar las librerías que se tienen en el entorno de python global pip3 list.
# Listar todas las librerías de python instaladas por el usuario pip3 freeze.
# Verificar donde esta python y pip which python3 o which pip3

#ambiente virtual= https://platzi.com/clases/4261-python-pip/55130-usando-entornos-virtuales-en-python/