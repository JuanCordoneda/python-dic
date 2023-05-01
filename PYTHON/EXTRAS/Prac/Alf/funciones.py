'1'
def saludo():
    return('hola amiga!')
print(saludo())
.......................................................................................................................................
'2'
nombre=input('dime tu nombre: ')
def saludo(nombre):
    print('hola',nombre,'!!')
saludo(nombre)
.......................................................................................................................................
'3'
número=int(input('dime el número: '))
def factorial(número):
    print('el número factorial es:',número,'!')
    x=1
    for i in range(número):
        x *= i+1
    print(x)
factorial(número)
.......................................................................................................................................
'4'
c=int(input('precio factura: '))
b=int(input('porcentaje de iva: '))
def factura(c,b=21):
    a=(c * b) / 100.0
    return a+c
print(factura(c,b))
.......................................................................................................................................
'5'
radio = int(input('dime el radio de la circunsferencia: '))
altura= int(input('altura: '))
def area(radio):
    area= (2*3.14*radio**2)
    return area

def cilindro(radio, altura):

    print('area cilindro: ',area(radio)*altura)

print(area(radio))
cilindro(radio,altura)
.......................................................................................................................................
'6'
lista=[3,5,6,7,8,3,7,8,9,6,7]
def media(lista):
    a=sum(lista)
    b=len(lista)
    return a/b
print('la media de la lista es:',media(lista))
.......................................................................................................................................
'7'
lista=[3,5,6,7,8,3,7,8,9,6,7]
def media(lista):
    cuadrados=[]
    for x in lista:
        a=x**2
        cuadrados.append(a)
 
    print(lista)
    print(cuadrados)

media(lista)

.......................................................................................................................................
'8'
lista=[3,5,6,7,8,3,7,8,9,6,7]
def media(lista):
    cuadrados=[]
    for x in lista:
        a=x**2
        cuadrados.append(a)
    return cuadrados
media=media(lista)
def medio(lista,media):
    dic={}
    mediacion=sum(lista)/len(lista)
    varianza= (sum(media))/(len(lista))-(mediacion**2)
    desviacion=varianza**0.5
    dic.update({'media':media,'varianza':varianza,'desviacion':desviacion })
    return dic

print(media)
print(medio(lista,media))


.......................................................................................................................................
'9'
def mcd(n, m):
    rest = 0
    while(m > 0):
        rest = m
        m = n % m
        n = rest
    return n

def mcm(n, m):
    if n > m:
        greater = n
    else:
        greater = m
    while (greater % n != 0) or (greater % m != 0):
        greater += 1
    return greater

print(mcd(24,36))
print(mcm(24,36))
.......................................................................................................................................
'10'
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
