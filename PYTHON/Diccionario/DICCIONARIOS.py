#un diccionario está compuesto de llave,valor (key,value)
diccionario = {
    "IDE": "Integrated Development Environment",
    "OOP": "Object Oriented Programming",
    "DBMS": "Database Management System"
}
print( diccionario )

#largo
print(len(diccionario))

#accediendo a un elemento
print( diccionario["IDE"])

#otra forma, mismo resultado
print( diccionario.get("IDE"))

#modificando valores
diccionario["IDE"]= "Integrated development environment"
print(diccionario)

#iterar 
for termino in diccionario:
    print(termino)

for termino in diccionario:
    print(diccionario[termino])   
     
for valor in diccionario.values():
    print(valor)
    
#comprobando existencia de un elemento
print( "IDE" in diccionario)   

#agregar nuevos elementos
diccionario["PK"] = "Primary Key"
print ( diccionario )
 
#remover elementos
diccionario.pop("DBMS")
print( diccionario ) 

#limpiar 
diccionario.clear()
print(diccionario)

#eliminar por completo
del diccionario
#print( diccionario )

.......................................................................................................
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
.......................................................................................................
edades = {'juanjo': 35, 'pedro': 45, 'valeria': 24}
for nombre in edades:
    print(nombre + " tiene " + str(edades[nombre]) + "años.")
.......................................................................................................
edades={'A':20,'B':30,'C':24,'D':18}
for x in edades:
    print(x,edades.get(x))

print(edades.get('V',10))    #GET
print(edades['A'])          
edades.update({'B':50})      #MODIFICAR
edades.update({'E':50})      #AGREGAR
del edades['A']              #ELIMINAR
print(edades)
.......................................................................................................

'LEDD 4.7'
a=True
mat={'ingles':6,'matematica':8.5,'sisop':8,'ledd':7,'ingenieria':8}
while a:
    a=input('dime la metria que quieres saber:')
    print(mat.get(a,'No la has rendido todavía'))
    