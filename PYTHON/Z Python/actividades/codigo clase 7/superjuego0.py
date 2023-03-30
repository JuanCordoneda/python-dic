import pygame

pygame.init()

WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode([WIDTH, HEIGHT])

jugando = True
pos_x = int(WIDTH / 2)
pos_y = int(HEIGHT / 2)
radio = 45

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

    if pressed_key[pygame.K_w]:
        pos_y -= 10
        if pos_y < radio:
            pos_y = radio
    elif pressed_key[pygame.K_DOWN]:
        pos_y += 10
    elif pressed_key[pygame.K_RIGHT]:
        pos_x = pos_x + 10
        if pos_x > WIDTH - radio:
            pos_x = WIDTH - radio
    elif pressed_key[pygame.K_LEFT]:
        pos_x = pos_x - 10

    # redibujar pantalla

    blanco = (150, 100, 25)
    screen.fill(blanco)

    pygame.draw.circle(screen, (0, 0, 255), (pos_x, pos_y), radio)

    pygame.display.flip()

pygame.quit()
