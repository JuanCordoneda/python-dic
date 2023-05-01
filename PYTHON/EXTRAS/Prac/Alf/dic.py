'1'
d={'Euro':'€', 'Dollar':'$', 'Yen':'¥'}
x=input('dime la divisa: ')
print(d.get(x,'no se encontro la divisa'))
# ................................................................................................

'2'
con={}
a=input('dime tu nombre: ')
con.update({'nombre':a})
b=input('dime tu edad: ')
con.update({'edad':b})
c=input('dime tu dirección: ')
con.update({'dirección':c})
d=int(input('dime tu teléfono: '))
con.update({'teléfono':d})

print(con.get('nombre'), 'tiene' ,con.get('edad'), 'años, vive en ',con.get('dirección'), 'y su número de teléfono es' ,con.get('teléfono'))
................................................................................................
'EJ 3'
a={'Platano':1.35,'Manzana':0.80,'Pera':0.85,'Naranja':0.70}
b=True
while b:
    b=input('que fruta deseas? ')
    c=int(input('cuantos kilos? '))
    try:
        B=a.get(b)
        C=B*c
    except:
        C='PRECIO NO DISPONIBLE'
    print('la fruta',b,'con kilos',c,'tiene el precio de: ',C)
...................................................................................................

'EJ 4'
fecha ={}
meses = {1:'enero', 2:'febrero', 3:'marzo', 4:'abril', 5:'Mayo', 6:'junio', 7:'julio', 8:'agosto', 9:'septiembre', 10:'octubre', 11:'noviembre', 12:'diciembre'}
A=input('dime la fecha en formato dd/mm/aaaa: ')
A = A.split('/')
print(A[1])
print('Hoy es el día:',A[0],'. Del mes',meses.get(int(A[1])),'. Del año:',A[2])
...................................................................................................

'5'
a={'Matemáticas': 6, 'Física': 4, 'Química': 5}
i=-1 
for x in a:
    i+=1
    print(x,'tiene', 'de nota.',a.get(x)) 
...................................................................................................

'6'
A={}
a=input('dime tu nombre: ')
A.update({'nombre':a})
print(A)
b=input('dime tu dirección: ')
A.update({'direccion':b})
print(A)
c=int(input('dime tu edad: '))
A.update({'edad':c})
print(A)
d=input('dime tu color de pelo: ')
A.update({'pelo':d})
print(A)
e=input('que droga te gusta mas: ')
A.update({'droguita':e})
print(A)
'RTA 2'
person = {}
more = 'Si'
while more=='Si':
    key = input('¿Qué dato quieres introducir? ')
    value = input(key + ': ')
    person[key] = value
    print(person)
    more = input('¿Quieres añadir más información (Si/No)? ')

...................................................................................................


'7'
compras={}
precio=[]
a=True
while a:      
    a=input('artículo: ')
    try:
        b=int(input('precio: '))
    except:
        b=0
    compras.update({a:b})
    precio.append(b)

print(compras)
print('PRECIO TOTAL: $',sum(precio))

.......................................................................................................................................
'8'
t={}
a=True
while a:
    a=input('español: ')
    b=input('ingles: ')
    if a and b:
        t.update({a:b})
    else:
        break
print(t)

frase=input('dime la frase: ')

for x in frase.split():
    print(t.get(x,x),end=' ')

.......................................................................................................................................

'9'

'Escribir un programa que gestione las facturas pendientes de cobro de una empresa. '
'Las facturas se almacenarán en un diccionario donde la clave de cada factura será el número de factura y el valor el coste de la factura. '
'El programa debe preguntar al usuario si quiere añadir una nueva factura, pagar una existente o terminar. '
'Si desea añadir una nueva factura se preguntará por el número de factura y su coste y se añadirá al diccionario. '
'Si se desea pagar una factura se preguntará por el número de factura y se eliminará del diccionario.'
'Después de cada operación el programa debe mostrar por pantalla la cantidad cobrada hasta el momento y la cantidad pendiente de cobro.'
facturas={}
a=False
b=False
resp=input('quieres pagar(b),añadir(a), o terminar: ')
if resp=='a':
    a=True
    b=False

elif resp=='b':
    a=False
    b=True
else:
    print('programa terminado')
    print('facturas:',facturas)


while a:
    n=input('número de factura: ')
    try:
        p=int(input('dime el valor: '))
        facturas.update({n:p})
        print('facturas:',facturas)
    except:
        resp=input('quieres pagar(b),añadir(a), o terminar: ')
        if resp=='a':
            b=False
            a=True
        elif resp=='b':
            a=False
            b=True
        else:
            print('programa terminado')
            print('facturas:',facturas)
            for x in facturas:
                print('debes pagar la factura:',x,'con el valor: $',facturas.get(x))
                break

while b:
    print('facturas:',facturas)
    for x in facturas:
        print('debes pagar la factura:',x,'con el valor: $',facturas.get(x))
    try:
        pagar=input('que factura quieres pagar? ')
        del facturas[pagar]
        print('factura',pagar,'pagada')    
    except:
        print('programa terminado. Para volver, ejecuta denuevo el programa')
        for x in facturas:
                print('debes pagar la factura:',x,'con el valor: $',facturas.get(x))
        break
                

.......................................................................................................................................

'10'

clients = {}
option = ''
while option != '6':
    if option == '1':
        nif = input('Introduce NIF del cliente: ')
        name = input('Introduce el nombre del cliente: ')
        address = input('Introduce la dirección del cliente: ')
        phone = input('Introduce el teléfono del cliente: ')
        email = input('Introduce el correo electrónico del cliente: ')
        vip = input('¿Es un cliente preferente (S/N)? ')
        client = {'nombre':name, 'dirección':address, 'teléfono':phone, 'email':email, 'preferente':vip=='S'}
        clients[nif] = client
    if option == '2':
        nif = input('Introduce NIF del cliente: ')
        if nif in clients:
            del clients[nif]
        else:
            print('No existe el cliente con el nif', nif)
    if option == '3':
        nif = input('Introduce NIF del cliente: ')
        if nif in clients:
            print('NIF:', nif)
            for key, value in clients[nif].items():
                print(key.title() + ':', value)
        else:
            print('No existe el cliente con el nif', nif)
    if option == '4':
        print('Lista de clientes')
        for key, value in clients.items():
            print(key, value['nombre'])
    if option == '5':
        print('Lista de clientes preferentes')
        for key, value in clients.items():
            if value['preferente']:
                print(key, value['nombre'])
    option = input('Menú de opciones\n(1) Añadir cliente\n(2) Eliminar cliente\n(3) Mostrar cliente\n(4) Listar clientes\n(5) Listar clientes preferentes\n(6) Terminar\nElige una opción:')


