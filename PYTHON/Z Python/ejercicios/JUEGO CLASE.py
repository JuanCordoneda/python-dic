import pygame
pelota= int(input('seleccionar tamaño de la pelota: '))
velocidad= int(input('seleccionar velocidad de la pelota: '))
pygame.init()

WIDTH = 600 #ANCHO
HEIGHT = 600 #LARGO

screen = pygame.display.set_mode([WIDTH, HEIGHT])

#posicion pelota
jugando = True
pos_x = int(WIDTH / 2) #ancho
pos_y = int(HEIGHT / 2) #largo
radio = pelota

while jugando:

    for event in pygame.event.get():

        # procesar eventos

        # TODO: ver si alt f4 cierra el programa
        if event.type == pygame.QUIT:
            jugando = False
        
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            jugando = False

    # calcular la nueva posición de los personajes

    pressed_key = pygame.key.get_pressed()
#al parecer la derecha y abajo(+) es diferente a la izquierda y arriba(-) 
    if pressed_key[pygame.K_UP] or pressed_key[pygame.K_w]:
        pos_y -= velocidad
        if pos_y < radio:
            pos_y = radio
    elif pressed_key[pygame.K_DOWN] or pressed_key[pygame.K_s]:
        pos_y += velocidad
        if pos_y > HEIGHT - radio:
            pos_y = HEIGHT - radio  
    elif pressed_key[pygame.K_RIGHT] or pressed_key[pygame.K_d]:
        pos_x += velocidad
        if pos_x > WIDTH - radio:
            pos_x = WIDTH - radio
    elif pressed_key[pygame.K_LEFT] or pressed_key[pygame.K_a]:
        pos_x -= velocidad
        if pos_x < radio:
            pos_x = radio
       

    # redibujar pantalla

    amarillo = (255, 255, 0)
    screen.fill(amarillo)

    pygame.draw.circle(screen, (colorpelota), (pos_x, pos_y), radio)

    pygame.display.flip()

pygame.quit()
