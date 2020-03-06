import pygame
import sys
import random
from math import sin
from time import sleep

pygame.init()

# Sizing
WIDTH = 50
HEIGHT = 50
RESOLUTION = 7
GAP = 3

# Colours
DEAD = 50, 50, 50
BACKGROUND = 0, 0, 0

glider = [
    ['DEAD', 'LIVE', 'DEAD'],
    ['DEAD', 'DEAD', 'LIVE'],
    ['LIVE', 'LIVE', 'LIVE']
]


def neighbours(arr, x, y):
    n = []
    for yOff in range(-1, 2):
        for xOff in range(-1, 2):
            if yOff == 0 and xOff == 0:
                pass
            else:
                row = ((yOff + y) + len(arr)) % len(arr)
                col = ((xOff + x) + len(arr[0])) % len(arr[0])
                n.append(arr[row][col])
    return n


def create2DArray(columns, rows):
    arr = []
    for i in range(rows):
        arr.append([])
        for j in range(columns):
            arr[i].append('')
    return arr


# Window Setup
size = screenWidth, screenHeight = (RESOLUTION + GAP) * WIDTH + GAP, \
                                   (RESOLUTION + GAP) * HEIGHT + GAP
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Game of Life')

grid = create2DArray(WIDTH, HEIGHT)
for x in range(WIDTH):
    for y in range(HEIGHT):
        grid[y][x] = random.choice(['DEAD', 'LIVE'])

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    screen.fill(BACKGROUND)

    for i in range(3):
        # Draw Grid
        x = y = 0
        while y < HEIGHT:
            while x < WIDTH:

                colour = BACKGROUND
                if grid[y][x] == 'DEAD':
                    colour = DEAD
                elif grid[y][x] == 'LIVE':
                    f = 0.2
                    colour = sin(f * y + 0) * 127 + 128, sin(f * y + 2) * 127 + 128, sin(f * y + 4) * 127 + 128

                row = (x * RESOLUTION) + (GAP * x) + GAP
                col = (y * RESOLUTION) + (GAP * y) + GAP
                pygame.draw.rect(screen, colour, (row, col, RESOLUTION, RESOLUTION))

                x += 1
            y += 1
            x = 0

        # Update Grid
        nextGrid = create2DArray(WIDTH, HEIGHT)

        for y in range(HEIGHT):
            for x in range(WIDTH):
                live = 0
                for c in neighbours(grid, x, y):
                    if c == 'LIVE':
                        live += 1

                state = grid[y][x]

                if state == 'DEAD' and live == 3:
                    nextGrid[y][x] = 'LIVE'
                elif state == 'LIVE' and (live < 2 or live > 3):
                    nextGrid[y][x] = 'DEAD'
                else:
                    nextGrid[y][x] = state

        grid = nextGrid

    pygame.display.update()
    sleep(0.1)
