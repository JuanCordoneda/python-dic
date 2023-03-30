a = 'excepciones'
try:
    prin
except:
    print('Los strings son inmutables')
finally:          #el finaly se ejecuta SIEMPRE
    print('escribi bien')    
    exit()
.......................................................................................
a= 'excepciones'
try:
    s[0]= 'E'
except NameError:
    print('que hace') 
try:
    1+'0'
except TypeError:
    print('que hace')
try:
    "hol".append("a")
except AttributeError:
    print('que hace')

....................................................................................................
try:
    1+'0'
    s[0]= 'E'
    "hol".append("a")
except NameError:
    exit()
except TypeError:
    exit()
except AttributeError:
    exit()

........................................................................................
'EJ 3'
try: HORA=float(input('dime la hora: '))
except:
    print("HORA EQUIVOCADA")
    print('la ahora ahora será, 11AM')
    HORA=11.00
if HORA<=12.59 and HORA>=00.00:
    print('MAÑANA')
elif HORA>=13.00 and HORA<=19.59:
    print('TARDE')
elif HORA>=20.00 and HORA<=23.59:
    print('NOCHE')
.............................................................................

from datetime import datetime, date, time, timedelta
import calendar
h=int(input('dime la hora: '))
m= int(input('ahora los minutos: '))
try: horario=time(h,m)
except:
    print('Hora errónea, ahora serán las 12PM')
    horario=time(12,00)
if horario<=time(12,30) and horario>=time(6,00):
    print('MAÑANA')
elif horario>=time(12,31) and horario<=time(19,00):
    print('TARDE')
elif horario>=time(19,1) and horario<=time(00,00):
    print('NOCHE')
elif horario>=time(00,1) and horario<=time(5,59):
    print('NOCHE')
.................................................................................