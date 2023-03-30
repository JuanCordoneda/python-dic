a= 0
b= 1 
while b < 10:
 print (b)
 
 a, b = b, a+b


......................................................................
a, b = 0, 1
while b < 1000:
 print(b)
 a, b = b, a+b

......................................................

edad= int(input('introduce tu edad por favor:' ))
intentos=0
while edad < 18 or edad > 100:
 print('eres menor para entrar a este sitio. Vuelve a intentarlo')
 if intentos>=1:
     print('\n no tienes mas intentos \n')
     break
    
 edad= int(input('introduce tu edad por favor:' ))
 intentos=intentos+1

print('Puedes entrar')
...................................................................................................

'EJ 5'
lista={}
no=input('dime tu nombre: ')
cantidad=int(input('dime la cantidad de materias: '))
contador=1
while cantidad>=contador:
    contador+=1
    m=input('materia: ')
    n=input('nota: ')
    lista.update({m:n})  
    print('mi nombre es:',no,'    materia:',m,'     nota:',n)
print(lista)

...................................................................................................

'Permitaencontrarelmenornúmeromayorqueceroqueesalavezmúltiplode 7, 11 y 1008.'
i=1
contador=0
while i:
    i+=1
    if i%7==0 and i%11==0 and i%1008==0:
        contador+=1
        print('el número es :',i)
        if contador==2:                     
            break
