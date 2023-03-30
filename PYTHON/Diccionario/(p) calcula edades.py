from datetime import *

f='6/10/1999'
def edad(fecha):
    hoy = date.today()
    fechanacimiento=fecha
    fechanacimiento = datetime.strptime(fechanacimiento, "%d/%m/%Y")
    edad = hoy.year - fechanacimiento.year - ((hoy.month, hoy.day) < (fechanacimiento.month, fechanacimiento.day))
    #primero restamos los años y luego restamos la comparación entre mes y día actual y mes y día de nacimiento. 
    print(edad)
edad(f)