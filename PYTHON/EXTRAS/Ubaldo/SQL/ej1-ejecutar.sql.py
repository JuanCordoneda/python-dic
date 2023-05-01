import psycopg2

conexion = psycopg2.connect(user='postgres',
                 password='admin',
                 host='127.0.0.1',
                 port='5432',
                 database='test_db')                #nombre de la database

cursor = conexion.cursor()                                     #este comando 'cursor' te deja leer datos de una base de datos. es el permiso
sentencia = 'SELECT * FROM persona'                            
cursor.execute(sentencia)                                      #el cursor ejecuta la sentencia
registros = cursor.fetchall()                                  #fetchall hace que se muestre toda la info del comando
print(registros)                                               #se imprime fetchall para ver el reistro 

cursor.close()
conexion.close()
