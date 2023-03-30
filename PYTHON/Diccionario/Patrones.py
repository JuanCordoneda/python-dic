lista=[1, 2, 3, 4, 5]
for i in lista:
    print(i*'+')

.....................................................................
for n in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
    print(n*str(n))
...................................................................
for n in [1, 2, 3, 4, 5]:
    print(n*'*')
for n in [5, 4, 3, 2, 1]:
    print(n*'*') 
..............................................................................
'EJ 14'
def triangulo(espacio,mas):
    print (espacio*" ",mas*"+")
triangulo(0,11)
triangulo(1,8)
triangulo(2,6)
triangulo(3,4)
triangulo(4,2)
..............................................................................

def piramide(num):
    lista=[]
    x=0
    for n in range(1,num):
        print(n*'*')


piramide(5) 