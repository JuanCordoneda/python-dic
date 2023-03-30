import random


def leer_valor_usuario()
    try:
        x = int(input('Adiviná: '))
    except:
        print("Valor erroneo, elijo por vos.")
        x = 10
    
    return x


def juego(nivel=1):

    print("NIVEL: ", nivel)
    
    salir = False
    
    secreto = random.choice(range(10 * nivel))
    print(secreto)
    intentos = []
    intento = leer_valor_usuario()
    while intento != secreto:
        if len(intentos) == 4:
            print("Perdiste!!!!!!!!!!")
            salir = True
            break
        intentos.append(intento)
        if intento > secreto:
            print('Más chico!')
        else:
            print('Más grande!')
        
        intento = leer_valor_usuario()
        print(intentos)

    else:
        print('Adivinaste!')

    intentos.append(intento)
    print('Intentos: {0}'.format(intentos))
    return salir
