import pygame

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

pygame.display.init()
up = 790
down = 1520
windows = pygame.display.set_mode((down, up))


class Block(pygame.sprite.Sprite):
    def __init__(self, color, x, y):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.speed = 15


block1 = Block((90, 150, 78), 1400, 700)
block2 = Block((225, 189, 45), 500, 500)
player = Block((145, 145, 145), 200, 100)
block4 = Block((12, 89, 225), 700, 600)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player.rect.left > 0 + 10:
        player.rect.x -= player.speed
    if keys[pygame.K_RIGHT] and player.rect.right < down - 15:
        player.rect.x += player.speed
    if keys[pygame.K_UP] and player.rect.top > 0 + 10:
        player.rect.y -= player.speed
    if keys[pygame.K_DOWN] and player.rect.bottom < up - 10:
        player.rect.y += player.speed

    windows.fill((50, 50, 50))
    windows.blit(block1.image, block1.rect)
    windows.blit(block2.image, block2.rect)
    windows.blit(player.image, player.rect)
    windows.blit(block4.image, block4.rect)
    pygame.display.flip()
    pygame.time.Clock().tick(60)

pygame.quit()
