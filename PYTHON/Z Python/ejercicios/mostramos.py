import random

def juego(nivel=1):

    print("NIVEL: ", nivel)

    secreto = random.choice(range(10 * nivel))
    intentos = [0]
    intento = int(input('Adiviná: '))
    while intento != secreto:
        intentos.append(intento)

        if intento > secreto:
            print('Más chico!')
        else:
            print('Más grande!')
        intento = int(input('Adiviná: '))

        if len(intentos) > 4:
             print("Perdiste!!!!!!!!!!")
             print(f'\nla respuesta era: {secreto}\n')
             break
    else:
        print('Adivinaste!')

    intentos.append(intento)
    print('Intentos: {0}'.format(intentos))
