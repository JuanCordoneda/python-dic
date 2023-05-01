import time
import random
def juego(nivel=1):
 palabras=['programacion', 'desarrollar', 'codigo', 'windows', 'python', 'bucle', 'error', 'software', 'condicion', 'hardware',]
 palabrarandom= random.choice(palabras)
 print("NIVEL: ", nivel)
 decision= input('quieres jugar? [si,no]:  ')        #decision
  
 time.sleep(0.5)
 if decision== 'si':
  print(' ')
  print("NIVEL: ", nivel)
  time.sleep(1)                            #palabras=lista de palabras
  print('comienza a adivinar')
  time.sleep(0.5)                          #palabra=palabrarandom
  tupalabra=' '                             #tupalabra= palabra seleccionada
  vidas=7

  while vidas>0:
    fallas=0
    for tuletra in palabrarandom:           #tuletra=letra seleccionada
        if tuletra in tupalabra:
            print(tuletra, end='')
        else:
            print('*',end='')
            fallas+=1
    if fallas==0:
        print('')
        print(' era la palabra. ganaste')
        break
    tuletra=input('      introduce una letra: ')
    tupalabra+= tuletra

    if tuletra not in palabrarandom:
        vidas-=1
        print('equivocación')
        print('tu tienes ',+vidas,' vidas')
    if vidas == 0:
        print('perdiste')
        print('la palabra era: ', palabrarandom)
        
  else:
      print('vuelve a intentarlo')
      exit()
    
 elif decision=='no':
     print('hasta luego')
     exit()