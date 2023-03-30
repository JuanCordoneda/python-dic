from JUEGO2 import juego
nombre= input('hola, cual es tu nombre?   ')
print ('hola', nombre)
nivel = 1

while True:
    juego(nivel)
    nivel = nivel +1