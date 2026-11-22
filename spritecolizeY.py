import random

import pygame

WHITE = (0, 0, 0)
BLACK = (255, 255, 255)
YELLOW = (216, 231, 49)
RED = (255, 0, 0)
GREEN = (66, 255, 25)

up = 790
down = 1520

pygame.init()
windows = pygame.display.set_mode((down, up))


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.center = (down // 2, up // 2)
        self.speed = 5

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.rect.left > 0 + 10:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT] and self.rect.right < down - 15:
            self.rect.x += self.speed
        if keys[pygame.K_UP] and self.rect.top > 0 + 10:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN] and self.rect.bottom < up - 10:
            self.rect.y += self.speed


class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.speedx = 3
        self.speedy = 3

    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        if self.rect.left <= 0 or self.rect.right >= down:
            self.speedx *= -1
        elif self.rect.top <= 0 or self.rect.bottom >= up:
            self.speedy *= -1


class Coin(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill(YELLOW)
        pygame.draw.circle(self.image, YELLOW, (15, 15), 15)
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)


grupa_all = pygame.sprite.Group()
grupa_coins = pygame.sprite.Group()
grupa_enemy = pygame.sprite.Group()
player = Player()
grupa_all.add(player)
for e in range(4):
    x = random.randint(0, down - 30)
    y = random.randint(0, up - 30)
    coin = Coin(x, y)
    grupa_coins.add(coin)
    grupa_all.add(coin)
for e in range(4):
    x = 100 * e
    y = 0
    enemy = Enemy(x, y)
    grupa_enemy.add(enemy)
    grupa_all.add(enemy)

score = 0

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    coin_hits = pygame.sprite.spritecollide(player, grupa_coins, True)
    for w in coin_hits:
        score += 10
        print("вам +10")
        x = random.randint(0, down - 30)
        y = random.randint(0, up - 30)
        coin = Coin(x, y)
        grupa_coins.add(coin)
        grupa_all.add(coin)

    enemy_hits = pygame.sprite.spritecollide(player, grupa_enemy, False)
    if enemy_hits:
        print('вам -10')
        score -= 10
    windows.fill((50, 50, 50))
    grupa_all.update()
    grupa_all.draw(windows)
    font = pygame.font.SysFont('arial', 36)
    text = f'очки {score}'
    text_end = font.render(text, True, (100, 0, 50))
    windows.blit(text_end, (30, 20))
    pygame.display.flip()
    pygame.time.Clock().tick(180)

pygame.quit()
