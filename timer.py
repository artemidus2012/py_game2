import random
import pygame

pygame.init()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (216, 231, 49)
RED = (255, 0, 0)
GREEN = (66, 255, 25)
BG_COLOR = (45, 90, 225)

DOWN = 1200
UP = 700

windows = pygame.display.set_mode((DOWN, UP))
pygame.display.set_caption("Сбор бонусов")
clock = pygame.time.Clock()
font = pygame.font.Font(None, 36)


class Bonus(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((40, 40))
        self.image.fill(YELLOW)
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.center = (DOWN // 2, UP // 2)
        self.speed = 7

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.rect.left > 10:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT] and self.rect.right < DOWN - 10:
            self.rect.x += self.speed
        if keys[pygame.K_UP] and self.rect.top > 10:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN] and self.rect.bottom < UP - 10:
            self.rect.y += self.speed


class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.speedx = random.choice([-5, 5])
        self.speedy = 5

    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy

        if self.rect.left <= 0 or self.rect.right >= DOWN:
            self.speedx *= -1
        if self.rect.top <= 0 or self.rect.bottom >= UP:
            self.speedy *= -1


grupa_all = pygame.sprite.Group()
grupa_bonus = pygame.sprite.Group()
grupa_enemy = pygame.sprite.Group()

player = Player()
grupa_all.add(player)

SPAWN_ENEMY_EVENT = pygame.USEREVENT + 1
pygame.time.set_timer(SPAWN_ENEMY_EVENT, 2000)

SPAWN_BONUS_EVENT = pygame.USEREVENT + 2
pygame.time.set_timer(SPAWN_BONUS_EVENT, 1500)

enemy_count = 0
score = 0
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == SPAWN_ENEMY_EVENT:
            ex = random.randint(50, DOWN - 100)
            enemy = Enemy(ex, 10)
            grupa_enemy.add(enemy)
            grupa_all.add(enemy)
            enemy_count += 1

        elif event.type == SPAWN_BONUS_EVENT:
            bx = random.randint(20, DOWN - 60)
            by = random.randint(20, UP - 60)
            bonus = Bonus(bx, by)
            grupa_bonus.add(bonus)
            grupa_all.add(bonus)

    grupa_all.update()

    hit_bonus = pygame.sprite.spritecollide(player, grupa_bonus, True)
    for _ in hit_bonus:
        print("Эй ты, атата, я на это время трачу!")
        score += 1

    if pygame.sprite.spritecollide(player, grupa_enemy, False):
        print(f"Игра окончена! Итоговый счет: {score}")
        running = False

    windows.fill(BG_COLOR)
    grupa_all.draw(windows)

    text = f"Врагов: {enemy_count} | Монет собрано: {score}"
    render_text = font.render(text, True, WHITE)
    windows.blit(render_text, (20, 20))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
