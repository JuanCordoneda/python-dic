import psycopg2 as db

conexion = db.connect(user='postgres',
                 password='admin',
                 host='127.0.0.1',
                 port='5432',
                 database='test_db')

cursor = conexion.cursor()
sentencia = 'INSERT INTO persona(nombre, apellido, apodo) VALUES(%s, %s, %s)'
valores = ('Carlos','Lara','pupe')
cursor.execute(sentencia, valores)
#guardamos la información en la base de datos
conexion.commit()                              #es necesario guardarlo cuando trabajamos con SELECT
registros_insertados = cursor.rowcount     #CON ESTE COMANDO PODEMOS VER LA CANTIDAD DE REGISTROS QUE SE INSERTARON
print(f'Registros insertados: {registros_insertados}')

cursor.close()
conexion.close()