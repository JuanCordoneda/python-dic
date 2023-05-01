from dominio.pelicula import Pelicula
from servicio.catalogopeliculas import Catalogo_peliculas
a=True
print('OPCIONES DE USUARIO:\n')
while a==True:  
    print('1.AGREGAR PELÍCULA.\n2.LISTAR PELÍCULAS.\n3.ELIMINAR PELÍCULAS.\n4.TERMINAR EL PROGRAMA.\n')
    dec=input('SELECCIONAR OPCIÓN (1-4): ')
    if dec=='1':
        try:
            Catalogo_peliculas.agregar_pelicula()
        except Exception as e:     
            print('ocurrió un error',e) 
    elif dec=='2':
        try:
            Catalogo_peliculas.listar_pelicula()
        except Exception as e:     
            print('ocurrió un error',e) 
    elif dec=='3':
        try:
            Catalogo_peliculas.eliminar_pelicula()
        except Exception as e:     
            print('ocurrió un error',e) 
    else:
        print('programa terminado.')
        break
