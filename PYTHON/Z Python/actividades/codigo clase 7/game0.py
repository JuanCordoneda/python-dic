import pygame

pygame.init()

screen = pygame.display.set_mode([800, 600])

running = True

while running:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

    screen.fill((255, 255, 255))

    pygame.draw.circle(screen, (0, 0, 255), (100, 100), 75)

    pygame.display.flip()


pygame.quit()