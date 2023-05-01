import time
import random
def juego(nivel=1):
 palabras=['programacion', 'desarrollar', 'codigo', 'windows', 'python', 'bucle', 'error', 'software', 'condicion', 'hardware',]
 palabrarandom= random.choice(palabras)

 decision= input('queres jugar al ahorcado? [si,no]:  ')        #decision
  #decisión si
 time.sleep(0.5)
 if decision== 'si':
  print(' ')
  print("NIVEL: ", nivel)
  time.sleep(1)                            #palabras=lista de palabras
  print('comenzá a adivinar')
  time.sleep(0.5)                          #palabra=palabrarandom
  tupalabra=' '                             
  vidas=7
#cuando la letra esta en la palabra
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
    tuletra=input('      introducí una letra: ')
    tupalabra+= tuletra
#cuando la letra no se encuentra en la palabra
    if tuletra not in palabrarandom:
        vidas-=1
        print('equivocación')
        print('tenés ',+vidas,' vidas')
    if vidas == 0:
        print('perdiste')
        print('la palabra era: ', palabrarandom)
        
  else:
      print('volvé a intentarlo')
      exit()
 #decision no   
 elif decision=='no':
     print('hasta luego')
     exit()


