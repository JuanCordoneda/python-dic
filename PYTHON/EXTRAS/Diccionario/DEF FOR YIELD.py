'el uso del *'
def devuelveciuades(*ciudades):
    for elemento in ciudades:
        yield elemento
ciuadesdevueltas=devuelveciuades('buenos aires','santa fe', 'rosarios','cordoba')
print(next(ciuadesdevueltas))
print(next(ciuadesdevueltas))
print(next(ciuadesdevueltas))
print(next(ciuadesdevueltas))


'subelementos'
def devuelveciuades(*ciudades):
    for elemento in ciudades:
        for subelemento in elemento:
            yield subelemento
ciuadesdevueltas=devuelveciuades('buenos aires','santa fe', 'rosarios','cordoba')
print(next(ciuadesdevueltas))
print(next(ciuadesdevueltas))
print(next(ciuadesdevueltas))
print(next(ciuadesdevueltas))
print(next(ciuadesdevueltas))
print(next(ciuadesdevueltas))
print(next(ciuadesdevueltas))
print(next(ciuadesdevueltas))
print(next(ciuadesdevueltas))
print(next(ciuadesdevueltas))
print(next(ciuadesdevueltas))
print(next(ciuadesdevueltas))


'subelementos sin next'
def devuelveciuades(*ciudades):
    for elemento in ciudades:
        for subelemento in elemento:
            yield subelemento
ciuadesdevueltas=devuelveciuades('buenos aires',' santa fe', ' rosario',' cordoba')
for i in ciuadesdevueltas:
    print(i)


'reemplazando el for anidado con el FROM''mismo resultado menos codigo''elemento puede ser (i)'
def devuelveciuades(*ciudades):
    for elemento in ciudades:
        # for subelemento in elemento:
        yield from elemento
ciuadesdevueltas=devuelveciuades('buenos aires',' santa fe', ' rosario',' cordoba')
for i in ciuadesdevueltas:
    print(i)

