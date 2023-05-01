# 'SET'
# print({1,2,3,4,5,3,4,})
# print(set([1,1,1,2,3,3,3,3])) #no acepta elem repetidos

# letras='juanjo'
# print(set('juanjo'))      #salen desordenados pero no repetidos
# pares={2,4,6,8,10,12,14}
# multiplos3={3,6,9,12,15}
# print(pares | multiplos3)  #funciona como +
# print(pares - multiplos3)
# print(pares & multiplos3)  #interseccion
# print(multiplos3 - pares)

# .............................................................................................
# #set es una colección sin orden y sin índices, no permite elementos repetidos
# #y los elementos no se pueden modificar, pero si agregar nuevos o eliminar
# planetas = {"Marte", "Júpiter", "Venus"}
# print(planetas)

# #largo
# print(len(planetas))

# #revisar si un elemento está presente
# print( "Marte" in planetas)

# #agregar
# planetas.add("Tierra")
# print( planetas )

# planetas.add("Tierra")#no se pueden agregar elementos duplicados
# print(planetas)

# #eliminar con remove posiblemente arroja excepción
# planetas.remove("Tierra")
# print(planetas)

# #eliminar con discard no arroja excepción
# planetas.discard("Júpiters")
# print( planetas )

# #limpiar el set
# planetas.clear()
# print( planetas )

# #eliminar el set
# del planetas
# #print( planetas )
# .............................................................................................

# ................................................................................................


# lista=[1,3,5,7,8,9]
# a=tuple(lista)   #tupla
# b=set(lista)     #conjunto
# print(a,b)
# .........................................................................

# .........................................................................

'LEDD 4.6'
con5={5,10,15,20,25,30,35,40,45,50}
con7={7,14,21,28,35,42,49,56,63,70,77,84,91,98,105}
print(con5&con7)
print(con5|con7)
print(con5-con7)
print(con7-con5)



