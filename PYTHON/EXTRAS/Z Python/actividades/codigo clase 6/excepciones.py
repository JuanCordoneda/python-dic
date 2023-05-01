print("Felicitaciones! Se garaon 1000000 de dolares!")

try:
    valor = int(input("¿Cuantos amigos son?: "))
    cada_uno = 1000000 / valor
except ZeroDivisionError:
    print("No puedo dividir por cero")
    cada_uno = 'infinito'
except:
    print("Ingrese un entero")
    cada_uno = 0

print("A cada uno le toca", "%0.2f" % cada_uno)
