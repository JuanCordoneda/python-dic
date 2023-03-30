import logging

# Variable logger a utilizar
logger = logging

logger.basicConfig(level=logging.DEBUG,                                 #se muestran mensajes desde el nivel DEBUG (NIVEL 1)
                   format='%(asctime)s: %(levelname)s [%(filename)s:%(lineno)s] %(message)s',   #FORMATO DEL MENSAJE A TRANSMITIR
                   datefmt='%I:%M:%S %p',                       #FORMATEO DEL MOMENTO EN EL QUE SE ESCRIBIO EL MENSAJE (PUEDE ESTAR O NO)
                   handlers=[                                   #LOS HANDLER SIRVEN PARA PASAR MENSAJES A UN ARCHIVO DE TEXTO O A LA CONSOLA
                       logging.FileHandler('capa_datos.log'),     #PASAR LA INFO AL ARCHIVO capa_datos.log
                       logging.StreamHandler()                    #PASAR LA INFO A LA TERMINAL
                   ]
                )

if __name__ == '__main__':   #ESTO SIRVE PARA EJECUTAR ACCIONES SIN MOD LA BASE DE DATOS
    logging.debug('mensaje a nivel debug')                   #NIVEL 1
    logging.info('mensaje a nivel info')                     #NIVEL 2
    logging.warning('mensaje a nivel warning')               #NIVEL 3
    logging.error('mensaje a nivel error')                   #NIVEL 4
    logging.critical('mensaje a nivel critical')             #NIVEL 5
    logging.debug('se realizó la conexión con exito')        

'SIEMPRE QUE SE USEN, SE MANDARA LA INFO A LA TERMINAL Y A capa_datos.py POR LOS HANDLERS'