numero = int(input("\nIngresa un número entero, por favor: "))

if numero < 0:
    numero = 0
    print ('El número ingresado es negativo cambiado a cero.')
elif numero == 0:
    print ('El número ingresado es 0.')
elif numero == 1:
    print ('El número ingresado es 1.')
else:
    print ('El número ingresado es mayor que uno.')
 .......................................................................................
'EJ 9'
num1=int(input('escribir número entero: '))
num2=int(input('escribir número entero: '))
num3=int(input('escribir número entero: '))
valores=[num1,num2,num3]
valores.sort()
print(valores) 
.......................................................................................
'EJ 10'
num1=int(input('escribir número entero: '))
num2=int(input('escribir número entero: '))
num3=int(input('escribir número entero: '))
valores=[num1,num2,num3]
valores.sort(reverse=True)
print(valores) 
