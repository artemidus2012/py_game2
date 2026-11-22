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
        self.speedx = 2
        self.speedy = 2

    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        if self.rect.left <= 0 or self.rect.right >= down:
            self.speedx *= -1
        elif self.rect.top <= 0 or self.rect.bottom >= up:
            self.speedy *= -1


grupa = pygame.sprite.Group()
colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (255, 0, 255)]
for e in range(4):
    x = 100
    y = 100
    sprite = Block(colors[e], x, y)
    grupa.add(sprite)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    grupa.update()

    windows.fill((50, 50, 50))
    grupa.draw(windows)
    pygame.display.flip()
    pygame.time.Clock().tick(450)

pygame.quit()
