'el get tira excepciones'


datos = {'Name': 'Zara', 'Age': 27}                       #GET

print (datos.get('Age'))
print (datos.get('Sex', "respuesta equivocada"))
.............................................................................

edades={'juanjo':35,'juan':20,'pedro':45,'valeria':43}
print(edades.get('juanjo'))                                   #GET
print(edades.get('jOSE','juan'))                                   
del edades['juanjo']                     #DEL
print(edades.get('juanjo','18'))
.............................................................................

edades = {'agustin': 28, 'pedro': 55, 'valeria': 24}
print(edades['agustin'])
print(edades.get('agustina', 0))
print(edades.get('agustin', 0))
edades['agustin'] = 29            #modificar
print(edades['agustin'])
edades['nuevo']=100       #agregar un elemento  
print(edades)
edades.update({'a':10,'b':40})   #otra forma de agregar
print(edades)
.............................................................................

materias={'lógica':6,'matematica':8,'sisop':7}
materia= input('dime la materia: ')
# print('tu nota es',materias[materia])
while materia:
    nota= materias.get(materia)
    if nota:
        print('tu nota es: ',nota)
    else:
        print('aun no se rindio')
    materia= input('dime la materia: ') 

.............................................................................
.............................................................................
.............................................................................
.............................................................................
.............................................................................

'EJ 4'
no=input('dime tu nombre: ')
l={'matematica':7,'logica':10,'ingles':5,'sistemas operativos':8}
le=tuple(l)
i=1
for i in range(4): 
    print('mi nombre es:',no,'   materia:',le[0+i],'   nota:',(l.get(le[0+i])))