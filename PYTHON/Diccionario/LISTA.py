rango = list( range(10) )
 
print(rango)
# ......................................................................................
lista=[1, 2, 3, 4, 5]
for i in lista:
    print(i*'+')
# # ......................................................................................
lista=[1,2,3,4,5]
print(sum(lista))                            #SUMAR COSAS EN LISTA
print(sum([3,6,9,8]))
# ...............................................................
print(set({1,2,3,4,5,7,3,6,9,0,0,0,0}))    #ordenar elem de una lista y saltear repetidos (DUDOSO CHECK ABAJO)


a=[4,55,66,12,23,4435,546,3,4,4534,5,45,5345,356]
a.sort()                              #ORDENAR ELEMENTOS DE UNA LISTA
print(a)

a=[4,55,66,12,23,4435,546,3,4,4534,5,45,5345,356]
a.sort(reverse=True)                         #ORDENAR ELEMENTOS DE UNA LISTA (INVERTIDOS)
print(a)

# ............................................................
c1=[1,2,3,4,5,7,3,6,9,0]
print(len(c1))                     #cantidad de elem de una lista
# ............................................................
pares={2,4,6,7,2}
mult={3,6,9}
print(pares.union(mult))          #unir 2 listas y ordenarlas
# ............................................................

datos = {'Name': 'Zara', 'Age': 27}                       #GET

print (datos.get('Age'))
print (datos.get('Sex', "respuesta equivocada"))
# .............................................................................
edades={'juanjo':35,'juan':20,'pedro':45,'valeria':43}
print(edades.get('juan'))                                   #GET
print(edades.get('jOSE','juan'))                                   
# .............................................................................
letras=['a','b','c','d','e','f']
print(letras[1])
letras.append('z')               #se le agrega un elemento
print(letras)
letras.extend(['r','s'])        #se le agrega una lista a la lista
print(letras)
letras= letras + ['i','j','k']   #otra forma de agregar elem a la lista
print(letras)
letras.pop(2)                    #quitar elem de una lista
letras.pop()                    #se quita el ultimo elemento
print(letras)
# .............................................................................
edades = {'agustin': 28, 'pedro': 55, 'valeria': 24}
print(edades['agustin'])
# .............................................................................
edades = {'juanjo': 35, 'pedro': 45, 'valeria': 24}
for nombre in edades:
  print(nombre + " tiene " + str(edades[nombre]) + "años.")
# .............................................................................
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
# # ............................................................................................................
lista=[5,8,20,3,4,5,2,3,23,35346,34,325,20000]
lista.sort()
for x in lista:
    print(x**2)                         #CUADRADO DE ELEMENTOS DE UNA LISTA
# # ............................................................................................................

lista=[5,8,20,3,4,5,2,3,23,35346,34,325,20000,33,545,6756,213,213,123,214,2354346,356,657,657,99999,1000000]
lista.sort()
pares=[]
                         #Imprima el cuadrado de los primeros diez números enteros pares.
for x in lista:
    if x%2==0:
        s=(x**2)
        print(s)
        pares.append(s)            
        if len(pares)>=10:
            break
print(pares)
# # ............................................................................................................

'INTERSECCION LISTAS'
autores_argentinos = ["Borges", "Saer", "Cortazar","Piglia", "Kohan", "Fogwill", "Casas"]
autores_extranjeros = ["Joyce", "Poe", "Child", "Carver","Chandler", "Coetze", "Auster"]
autores_vivos = ["Casas", "Kohan", "Child", "Coetze","Auster"]
vivosarg=[autores_argentinos,autores_vivos]

resultado = []
for i in autores_argentinos:
    for j in autores_vivos:
           if i == j:
               resultado.append(i)

print(resultado)  