import pygame
import sys
import random


pygame.init()

up = 801
down = 1540
windows = pygame.display.set_mode((down,up))
pygame.display.set_caption('''pop''')
WHITE = (255,255,255)
BLACK = (0,0,0)
PINK = (229,32,118)
GREEN= (204,247,194)
BEIGE = (191,89,91)

running = True
while running :
    for event in pygame.event.get() :
        if event.type == pygame.QUIT :
            running = False
    windows.fill(WHITE)
    pygame.display.flip()
    pygame.time.Clock().tick(10)
pygame.quit()
sys.exit()
