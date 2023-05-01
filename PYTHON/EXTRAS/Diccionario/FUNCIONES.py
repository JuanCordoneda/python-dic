def generapares(limite):
    num=1
    milista=[]
    while num<limite:
        milista.append(num*2)
        num+=1
    return milista
print(generapares(10))

...................................................................
def generapares(limite):
    num=1
    while num<limite:
        yield(num*2)
        num+=1
    
devuelvepares=generapares(10)

for i in devuelvepares:
    print(i)

.........................................................................
'multiplos de 3'
def multiplo3(limite):
    contador=1
    while contador<limite:
        yield(contador*3)
        contador+=1
multiplos=multiplo3(11)
for i in multiplos:
    print(i)


..........................................................................
'alternativa multiplo 3 con next'
def multiplo3(limite):
    contador=1
    while contador<limite:
        yield(contador*3)
        contador+=1
multiplos=multiplo3(11)
print(next(multiplos))
print(next(multiplos))
print(next(multiplos))
print(next(multiplos))
print(next(multiplos))

.................................................................................
'EJ 14'
def triangulo(espacio,mas):
    print (espacio*" ",mas*"+")
triangulo(0,11)
triangulo(1,8)
triangulo(2,6)
triangulo(3,4)
triangulo(4,2)
.................................................................................

autores_argentinos = ["Borges", "Saer", "Cortazar","Piglia", "Kohan", "Fogwill", "Casas"]
autores_extranjeros = ["Joyce", "Poe", "Child", "Carver","Chandler", "Coetze", "Auster"]
autores_vivos = ["Casas", "Kohan", "Child", "Coetze","Auster"]
vivosarg=[autores_argentinos,autores_vivos]


def interseccion(autores_argentinos,autores_vivos):      #interseccion listas
    resultado = []
    for i in autores_argentinos:
        for j in autores_vivos:
           if i == j:
               resultado.append(i)      
    print(resultado)  

interseccion(autores_argentinos,autores_vivos)
..............................................................................

def piramide(num):
    lista=[]
    x=0
    for n in range(1,num):
        print(n*'*')


piramide(5) 


..............................................................................

def cualquiera(a, b, c, d=10, e=20):
    print(a, b*c, d + e)

cualquiera(10, 5, 6)
cualquiera(10, 5, 6, 5,10)
cualquiera(10, 5, 6, 1,1)
cualquiera(1, 5, 6)
cualquiera(1, 5, 4)
cualquiera(1, 5, 2)

...................................................................................
def tupla(*a):
    print(a)
tupla(1,2,3,5,6,7,8)              #GENERADOR DE TUPLAS

def diccionario(**b):
    print(b)
diccionario(a=10,b=20)           #GENERADOR DE DICCIONARIOS

def d(*a,**b):
    print(a,b)
d(1,'hola',3,4,a=20,b=30)          #MEZCLADOS



.......................................................................................

def validar_longitud_password(password):
    
    if len(password) > 5:
        return True
    else:
        return False
for x in range(3):
    a = input()
    print(validar_longitud_password(a))          #CANTIDAD DE VECES QUE EJECUTAS LA FUNCION


def validar_longitud_password(password, min_chars=5):      #PARAMETROS POR DEFECTO
    if len(password) > min_chars:
        return True
    else:
        return False

print(validar_longitud_password('hola',8))
print(validar_longitud_password('hola',3))
print(validar_longitud_password('hola'))


'CONTADOR DE PALABRAS'
a=input('caracteres: ')
def caracteres(a):
    dic={}      #SI LA PALABRA ESTA REPETIDA, SE LE SUMA 1
    for i in a.split():
        if i in dic:
            dic[i] += 1     
        else:
            dic[i] = 1
    return(dic)
