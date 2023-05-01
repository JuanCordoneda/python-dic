nombre='juan cruz'
for i in nombre:    
    if i==' ':
        continue
    print('nueva letra:,'+i)



contador=0
nombre='Pedro'
for i in nombre:
    if i=='o':
        continue
    contador+=1
    print(i)
print(contador)

for x in range(1000):
    if x % 13 != 0:
        continue #PASA A LA SGTE EJECUCION
    print(x, x ** 2)