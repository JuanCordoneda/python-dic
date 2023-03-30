import psycopg2

conexion = psycopg2.connect(user='postgres',
                 password='admin',
                 host='127.0.0.1',
                 port='5432',
                 database='test_db')                #nombre de la database


cursor = conexion.cursor()                                     #este comando 'cursor' te deja leer datos de una base de datos. es el permiso
sentencia = 'SELECT * FROM empleados'  
cursor.execute(sentencia)                                      #el cursor ejecuta la sentencia
registros = cursor.fetchall()                                  #fetchall hace que se muestre toda la info del comando
print(registros)                                               #se imprime fetchall para ver el reistro 

cursor.close()
conexion.close()
............................................................................................
cursor = conexion.cursor()                                     #este comando 'cursor' te deja leer datos de una base de datos. es el permiso
sentencia = 'SELECT * FROM empleados WHERE id_persona=%s'                            
id_persona=input('dime el id del funcionario: ')
tupla=(id_persona,)
cursor.execute(sentencia,tupla)                                      #el cursor ejecuta la sentencia

registros = cursor.fetchone()                                  #fetchall hace que se muestre toda la info del comando
print(registros)                                               #se imprime fetchall para ver el reistro 

cursor.close()
conexion.close()
............................................................................................

cursor=conexion.cursor()
sentencia='SELECT * FROM empleados WHERE id_persona IN %s'
entrada=input('dime las ids separadas por comas: ')
tupla = tuple(entrada.split(',')) 
tupl=(tupla,)
cursor.execute(sentencia,tupl)

registro=cursor.fetchall()
print(registro)

cursor.close()
conexion.close()
............................................................................................

cursor=conexion.cursor()
sentencia='INSERT INTO empleados(nombre,apellido,salario) VALUES(%s,%s,%s)'
valores = (
    ('Marcos','Cantu','56000'),
    ('Angel','Quintana','60000'),
    ('Marcos','Gonzalez','0')              #HAY QUE HACER UNA TUPLA CON TODOS LOS REGISTROS A AGREGAR
)
cursor.executemany(sentencia,valores)
conexion.commit()

registros_insertados = cursor.rowcount
print(f'Cantidad de Registros insertados: {registros_insertados}')

cursor.close()
conexion.close()
............................................................................................

cursor=conexion.cursor()
sentencia = 'UPDATE empleados SET nombre = %s, apellido = %s, salario = %s WHERE id_persona = %s'
valores = (
    ('Juan', 'Perez', '70000', 7),
    ('Karla1', 'Gomez2', '500000', 8)              #HAY QUE HACER UNA TUPLA CON TODOS LOS REGISTROS A MODIFICAR
)
cursor.executemany(sentencia, valores)                       #EXECUTEMANY
conexion.commit()

registros_actualizados = cursor.rowcount
print(f'Registros actualizados: {registros_actualizados}')

cursor.close()
conexion.close()
............................................................................................

cursor = conexion.cursor()
sentencia = 'DELETE FROM empleados WHERE id_persona = %s'
valores = (
    ('7'),('8'),('9')
)
cursor.executemany(sentencia, valores)
#guardamos la información en la base de datos
conexion.commit()

registros_eliminados = cursor.rowcount
print(f'Registros eliminados: {registros_eliminados}')

cursor.close()
conexion.close()