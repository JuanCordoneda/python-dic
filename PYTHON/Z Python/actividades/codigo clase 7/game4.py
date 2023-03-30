import pygame

from pygame.locals import K_ESCAPE, KEYDOWN, K_UP, K_DOWN, K_LEFT, K_RIGHT

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])

running = True
pos_x = 100
pos_y = 100
radio = 75

while running:

    for event in pygame.event.get():
        
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
        
        if event.type == pygame.QUIT:
            running = False


    pressed_keys = pygame.key.get_pressed()

    if pressed_keys[K_UP]:
        pos_y -= 1
    elif pressed_keys[K_DOWN]:
        pos_y += 1
    elif pressed_keys[K_LEFT]:
        pos_x -= 1
    elif pressed_keys[K_RIGHT]:
        pos_x += 1

    # TODO: que no se salga a la derecha y a abajo
    if pos_x < radio:
        pos_x = radio
    if pos_x > SCREEN_WIDTH:
        pos_x = SCREEN_WIDTH
    if pos_y < radio:
        pos_y = radio
    if pos_y > SCREEN_HEIGHT:
        pos_y = SCREEN_HEIGHT

    screen.fill((255, 255, 255))

    pygame.draw.circle(screen, (0, 0, 255), (pos_x, pos_y), radio)

    pygame.display.flip()


pygame.quit()