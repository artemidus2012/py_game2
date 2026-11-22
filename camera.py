import pygame




Clock = pygame.time.Clock

pygame.init()

down = 790
up = 1520

WORLD_WIDTH = 3000

WORLD_HATE = 3000

TILE_SIZE = 50

class Camera:


windows = pygame.display.set_mode((down, up))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    clock.tick(60)
    windows.fill((0, 0, 0))
    pygame.display.flip()
pygame.quit()