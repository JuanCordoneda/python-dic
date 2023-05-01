import psycopg2 as db

conexion = db.connect(user='postgres',
                 password='admin',
                 host='127.0.0.1',
                 port='5432',
                 database='test_db')

# cursor = conexion.cursor()
# sentencia = 'UPDATE persona SET nombre = %s, apellido = %s, apodo = %s WHERE id_persona = %s'
# valor = ('Juan1','Perez2','trolo', 8)
# cursor.execute(sentencia, valor)
# #guardamos la información en la base de datos
# conexion.commit()
# registros_actualizados = cursor.rowcount
# print(f'Registros actualizados: {registros_actualizados}')
# cursor.close()
# conexion.close()

#.............................................................................................................................
cursor = conexion.cursor()
sentencia = 'UPDATE persona SET nombre = %s, apellido = %s, apodo = %s WHERE id_persona = %s'
valores = (
    ('Juan', 'Perez', 'jperez@mail.com', 7),
    ('Karla1', 'Gomez2', 'kgomez3@mail.com', 8)              #HAY QUE HACER UNA TUPLA CON TODOS LOS REGISTROS A MODIFICAR
)
cursor.executemany(sentencia, valores)                       #EXECUTEMANY
# guardamos la información en la base de datos
conexion.commit()
registros_actualizados = cursor.rowcount
print(f'Registros actualizados: {registros_actualizados}')
cursor.close()
conexion.close()
