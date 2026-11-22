import pygame


сlock = pygame.time.Clock

pygame.init()

down = 790
up = 1520

windows = pygame.display.set_mode((down, up))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    сlock.tick(60)
    windows.fill((0, 0, 0))
    pygame.display.flip()
pygame.quit()