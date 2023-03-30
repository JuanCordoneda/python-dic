respuesta1= input('quieres saber que dia es hoy? ')
from datetime import date
hoy= date.today().strftime('%d,%m,%y')
print(f'{hoy}')
prespuesta2= input('quiere saber que hora es? ')
import time
hora= (time.strftime("%H:%M:%S"))
print(f'{hora}')
#....................................................................

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

