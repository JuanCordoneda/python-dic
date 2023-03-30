letras=['a','b','c','d','e','f']

inmutable=tuple(letras)      #ponemos a la lista en una tupla. estas son inmutables

print(inmutable[0])
# inmutable.append('z')     'no se puede modificar'

.............................................................................
edades = {'agustin': 28, 'pedro': 55, 'valeria': 24}
print(edades['agustin'])
.............................................................................
tupla='a','b','c'
for x in tupla:
 print(x.upper())
.............................................................................
'EJ 4'
no=input('dime tu nombre: ')
l={'matematica':7,'logica':10,'ingles':5,'sistemas operativos':8}
le=tuple(l)
i=1
for i in range(4): 
    print('mi nombre es:',no,'   materia:',le[0+i],'   nota:',(l.get(le[0+i])))
....................................................................................

lista=[1,3,5,7,8,9]
a=tuple(lista)   #tupla
b=set(lista)     #conjunto
print(a,b)

....................................................................................

'LEDD 4.3'
materias=[]
tu=True
nombre='juan'
while tu:
    tu=input('dime una materia: ')
    pla=input('ahora dime la nota: ')
    tupla=(tu,pla)
    if tu:
        materias.append(tupla)
        num=1
        for x in range(num):
            print('mi nombre es',nombre,'.   La nota de la materia:',tu,'   fue:',pla)

print(materias)

