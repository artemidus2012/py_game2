import pygame

pygame.init()
down = 790
up = 1520
BLACK = (225, 225, 225)
level_map = [
    "11111111111111111111",
    "10000000000000000001",
    "10222222222222222201",
    "10222222222222222201",
    "10222211112222222201",
    "10222211112222222201",
    "10222200002222222201",
    "10222200002222222201",
    "10222222222222222201",
    "10222222222222222201",
    "102222222322222201",
    "10222222222222222201",
    "10222222222222222201",
    "10000000000000000001",
    "11111111111111111111",
]

windows = pygame.display.set_mode((down, down))

clock = pygame.time.Clock()
TILE_SIZE = 40
TILE_COLORS = {0: (255, 241, 0),
               1: (195, 0, 131),
               2: (65, 219, 0),
               3: (225, 225, 0)}


class Tile(pygame.sprite.Sprite):
    def __init__(self, x, y, tile_type):
        super().__init__()
        self.image = pygame.Surface((TILE_SIZE, TILE_SIZE))
        self.image.fill(TILE_COLORS[tile_type])
        pygame.draw.rect(windows, BLACK, (0, 0, TILE_SIZE, TILE_SIZE), 1)
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.type = tile_type


class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((20, 20))
        self.image.fill((46, 22, 176))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.speed = 4

    def update(self, walls):
        key = pygame.key.get_pressed()
        old_x = self.rect.x
        old_y = self.rect.y
        if key[pygame.K_s]:
            self.rect.y += self.speed
        if key[pygame.K_w]:
            self.rect.y -= self.speed
        if pygame.sprite.spritecollide(self, walls, False):
            self.rect.y = old_y
        if key[pygame.K_d]:
            self.rect.x += self.speed
        if key[pygame.K_a]:
            self.rect.x -= self.speed
        if pygame.sprite.spritecollide(self, walls, False):
            self.rect.x = old_x


grupa_all = pygame.sprite.Group()
grupa_walls = pygame.sprite.Group()
grupa_can_go = pygame.sprite.Group()

for row_index, row in enumerate(level_map):
    for col_index, tile in enumerate(row):
        type_tile = int(tile)
        x = col_index * TILE_SIZE
        y = row_index * TILE_SIZE
        tile_sprite = Tile(x, y, type_tile)
        grupa_all.add(tile_sprite)
        if type_tile == 1:
            grupa_walls.add(tile_sprite)
        else:
            grupa_can_go.add(tile_sprite)

player = Player(90, 462)
grupa_all.add(player)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    player.update(grupa_walls)
    windows.fill((0, 0, 0))
    grupa_all.draw(windows)
    font = pygame.font.SysFont('None', 20)
    text = ['фиолетовый - стена', 'жёлтый - пристенная зона', 'зелёный - трава']
    render_text = font.render(text[0], 1, (195, 0, 131))
    windows.blit(render_text, (30, 650))
    render_text = font.render(text[1], 1, (255, 241, 0))
    windows.blit(render_text, (30, 700))
    render_text = font.render(text[2], 1, (65, 219, 0))
    windows.blit(render_text, (30, 750))
    pygame.display.flip()
    clock.tick(60)
pygame.quit()
