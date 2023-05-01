import psycopg2 as db

conexion = db.connect(user='postgres',
                 password='admin',
                 host='127.0.0.1',
                 port='5432',
                 database='test_db')

cursor = conexion.cursor()                            #permiso
sentencia = 'SELECT * FROM persona WHERE id_persona IN %s'                   
entrada = input("Proporciona las pk a buscar (separado por comas): ")       
tupla = tuple(entrada.split(','))                                           #creador de tupla
print(tupla)
llaves_primarias = (tupla,)                                      #meter la tupla dentro de otra tupla
cursor.execute(sentencia, llaves_primarias)                        #ejecutar la sentencia y la tupla de tuplas
registros = cursor.fetchall()                                    #imprimir TODOS los registros (fetchall)
print(registros)
# for registro in registros:
#     print(registro)

cursor.close()
conexion.close()