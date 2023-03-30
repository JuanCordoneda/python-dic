lado1= int(input('lado 1: '))
lado2= int(input('lado 2: '))
lado3= int(input('lado 3: '))
if lado1**2 + lado2**2==lado3**2:
 print('true')
#2
a='    * '
b='   *** '
c='  ***** '
d=' ******* '
for i in [ a , b, c, d]:
 print(i)
#4
radio = int(input('dime el radio de la circunsferencia: '))
área= (radio*3.14)
print(f'radio: {radio} ')
print(f'el área es {área}')
#5
d=int(input('dime la base'))
for n in [1, 2, 3, 4, 5, 6, 7, 8, d]:
    print(n*'*')
