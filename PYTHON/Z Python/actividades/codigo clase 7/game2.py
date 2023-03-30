import pygame

from pygame.locals import K_ESCAPE, KEYDOWN, K_UP, K_DOWN, K_LEFT, K_RIGHT

pygame.init()

screen = pygame.display.set_mode([800, 600])

running = True
pos_x = 100
pos_y = 100

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

    screen.fill((255, 255, 255))

    pygame.draw.circle(screen, (0, 0, 255), (pos_x, pos_y), 75)

    pygame.display.flip()


pygame.quit()