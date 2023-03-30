from mostramos import juego

#nivel = int(input("Ingrese el nivel: "))

nivel = 1

perdio = False

while not perdio:
    perdio = juego(nivel)
    nivel = nivel + 1
