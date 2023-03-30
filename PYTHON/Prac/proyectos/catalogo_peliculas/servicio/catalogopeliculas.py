import os
class Pelicula:
    def __init__(self,nombre):
        self.__nombre=nombre
    def __str__(self):
        return self.__nombre
    
    def get_nombre(self):
        return self.__nombre

class Catalogo_peliculas:  
    @staticmethod
    def agregar_pelicula():
        try:
            p=input('dime la película: ')
            pelicula=Pelicula(p)
            archivo = open("ruta_archivo.txt", "a")
            archivo.write(f'{pelicula.__str__()}\n')
        except Exception as e:     
            print('ocurrió un error',e) 
        finally:
            archivo.close()

    @staticmethod
    def listar_pelicula():
        try:
            archivo=open("ruta_archivo.txt",'r')
            print('LISTA DE PELICULAS:\n'+ archivo.read())
        except Exception as e:     
            print('ocurrió un error',e) 
        finally:
            archivo.close()

    @staticmethod
    def eliminar_pelicula():       
        try:
            os.remove('ruta_archivo.txt')
            print('archivo eliminado')
        except Exception as e:     
            print('ocurrió un error',e) 
        

# Catalogo_peliculas.agregar_pelicula()
# Catalogo_peliculas.agregar_pelicula()
# Catalogo_peliculas.agregar_pelicula()
# Catalogo_peliculas.listar_pelicula()
# Catalogo_peliculas.eliminar_pelicula()

