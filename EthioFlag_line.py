import pygame, sys
from pygame.locals import *

#initialize the pygame
pygame.init()
screen = pygame.display.set_mode((1200, 600))
clock = pygame.time.Clock()

#Color callouts (R, G, B)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 215, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GRAY = (100, 100, 100)
NAVYBLUE = ( 60, 60, 100)
ORANGE = (255, 128, 0)
PURPLE = (255, 0, 255)
CYAN = ( 0, 255, 255)

#Background
screen.fill(RED)
pygame.draw.rect(screen, GREEN, (0, 0, 1200, 200))
pygame.draw.rect(screen, YELLOW, (0, 200, 1200, 200))
pygame.draw.circle(screen, BLUE, (600, 300), 150, 150)

#Point 1 to 2
pygame.draw.line(screen, YELLOW, (600, 180), (667.14, 394.28), 4)
#Point 1 to 5
pygame.draw.line(screen, YELLOW, (600, 180), (531.43, 394.29), 4)
#Point 2 to 3
pygame.draw.line(screen, YELLOW, (667.14, 394.28), (497.14, 265.71), 4)
#Point 3 to 4
pygame.draw.line(screen, YELLOW, (497.14, 265.71), (711.43, 265.71), 4)
#Point 4 to 5
pygame.draw.line(screen, YELLOW, (711.43, 265.71), (531.43, 394.29), 4)
#Between 2 and 4
pygame.draw.line(screen, YELLOW, (667, 327.141), (714.86, 353.28), 4)

#Between 4 and 1
pygame.draw.line(screen, YELLOW, (640, 255), (687.14, 214.29), 4)

#Between 1 and 3
pygame.draw.line(screen, YELLOW, (565.71, 248.57), (531.43, 205.71), 4)

#Between 3 and 5
pygame.draw.line(screen, YELLOW, (548.57, 317.14), (497, 342.86), 4)

#Between 2 and 5
pygame.draw.line(screen, YELLOW, (600, 360), (600, 420), 4)

#Title and Icon
pygame.display.set_caption("Ethiopian Flag")
icon = pygame.image.load("ETHIO.png")
pygame.display.set_icon(icon)
window = True

#Game Loop

while window:
##    font = pygame.font.Sysfont('timesnewroman', 20)

    for event in pygame.event.get():
        if event.type == QUIT:
          pygame.quit()
##    return

    mouse = pygame.mouse.get_pos()
    print(mouse)
    pygame.display.update()
    clock.tick(60)

