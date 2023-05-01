import psycopg2 as db

conexion = db.connect(user='postgres',
                 password='admin',
                 host='127.0.0.1',
                 port='5432',
                 database='test_db')

cursor = conexion.cursor()                                    #permiso
sentencia = 'SELECT * FROM persona WHERE id_persona = %s'  #el signo %s sirve como comodín, este se va a modificar con una tupla
#id_persona = 2
id_persona = input("Proporciona la pk(llave primaria) a buscar [de 1 a 5]:") #aqui, el comodin se transforma en un input para luego convertirse en tupla
tupla = (id_persona,)              #para pasar un parametro en sql, hay que convertirlas en tupla. en python se hace con (tupla ,) la coma la convierte
cursor.execute(sentencia, tupla)    #ahi se pasa como parámetro
print(registros)

cursor.close()
conexion.close()