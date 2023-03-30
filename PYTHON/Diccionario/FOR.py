input('quieres saludar a el grupo keki?: ')
for i in ['tito','ñandu','juani']:
 print('hola ' +i+ ',falopero.', end= '    ')
##################
email=False
email=input('\n introduce tu email:  ')
for i in email:
 if (i=='@'):
     email==True
if email==True:
     print('\n el mail es correcto')
else: 
     print('el email no es correcto')   
###################  
contador=0
email=input('\n introduce tu email:  ')
for i in email:
 if (i=='@' or i=='.'):
      contador=contador+1
if contador==2:
     print('\n el mail es correcto')
else: 
     print('el email no es correcto')   
################### 
for i in range (5,51,5):
     print(f'hola{i}')

for i in range(len('número')):
     print(f'hola{i}')
###################
email=input('introduce tu mail')
for i in range(len(email)):
     if email[i]=='@':
          email=True

if email==True:
     print('el mail es correcto')
else:
     print('email incorrecto')
##################
'contador de numeros'
for i in range(1,101,1):
    print(i)
#################
'ej 9 ejercicios for cadena caracteres'
for i in 'hola mundo':
    print(i)
######################
'ej 10. genera pares'
for i in range(0,100,2):
    print(i)
######################
'ej 13. rango entre 10 y 1'
for i in range(10,0,-1):
    print(i)
#######################
'ej 14, rangos entre 10,1 y 15,20'
for i in range(10,0,-1):
    print(i)
for i in range (15,21):
        print(i)
############################
'ejercicio 4'
nombre=input('dime tu nombre: ')
numero=int(input('ahora dime la cantidad de veces que aparecer tu nombre: '))
for i in range(numero):
    print(nombre)
..............................................................
cuadrado=[(1,1),(1,10),(10,1),(10,10)]
for x in cuadrado:
    print(x[0],x[1])

print('...............................................')
for x,y in cuadrado:
    print(x,y,x+y)
print('...............................................')
for x in cuadrado:
    print(x)
...................................................................
número= int(input('dame tu edad: '))  #imprime un número por vuelta
for i in range(número):
    print(i)
print(número)

............................................................................
número= int(input('dame tu edad: '))    #cuenta los numeros para atras
for i in range (número):
    print(i,',',end='')
.................................................................................
total=1
for x in [3,7,8,9]:                'MULTIPLICAR'
    total=total*x
print(total)
.................................................................................
'potenciar'
for x in {2,5,7}:
    print(x**2)
.....................................................................................
edades = {'juanjo': 35, 'pedro': 45, 'valeria': 24}
for nombre in edades:
  print(nombre + " tiene " + str(edades[nombre]) + "años.")
for edad in edades.values():
  print("Hay personas con " + str(edad) + " años.")
.....................................................................................

tupla='a','b','c'
for x in tupla:
 print(x.upper())    #poner mayusculas
.....................................................................................
num=int(input('cantidad de materias:'))
for x in range(num):
    n=input('dime tu nombre: ')
    m=input('dime tu materia: ')
    print('mi nombre es:',n,'y curso:',m)

# .........................................................................
