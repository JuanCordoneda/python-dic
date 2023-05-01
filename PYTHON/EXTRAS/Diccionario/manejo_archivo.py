'WRITE'   'ESTE METODO SOBREESCRIBE ARCHIVOS'
try:
    archivo = open("prueba.txt", "w")
    archivo.write("Agregamos info al archivo\n")
    archivo.write("hola")
except Exception as e:     
    print('ocurrió un error',e) 
finally:
    archivo.close()
    #después de close ya no podemos trabajar con el archivo
    #archivo.write("saludos")

'APPEND' 'NO SOBREESCRIVE ARCHIVOS'
archivo = open("prueba.txt", "a")
archivo.write("Agregamos info al archivo\n")
archivo.close()

'ELIMINAR ARCHIVOS'
import os
os.remove('ruta_archivo.txt')


'READ'
archivo=open("prueba.txt",'r')
print(archivo.read())
print(archivo.readline())  #lee solo la primer línea
print(archivo.readlines())  #crea una lista con cada línea de nuestro archivo
print(archivo.read(5)) #'si pongo 5 ahi, la funcioin me va a leeer solo 5 caracteres'

archivo.close()

'para archivos que no estan en la misma carpeta, hay que copiar la ruta'
archivo=open("C:\\Users\\Usuario\\Desktop\\PYTHON\\Diccionario\\prueba.txt",'r')   #SIEMPRE CON DOBLE BARRA
print(archivo.read())
archivo.close()
    