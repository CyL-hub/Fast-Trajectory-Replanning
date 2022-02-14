

from repeatAstar import *
from maxRepeatAstar import *
from repeatBackwards import *
from maxRepeatBackwards import *
from repeatAdaptive import *
from maxRepeatAdaptive import *
import pygame, sys
from pygame.locals import *

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
BLUE = (135,206,235)

WIDTH = 7.5
HEIGHT = 7.5
MARGIN = 0.5

def visualize(ASTAR, TIEBREAK, WORLD):
    if int(WORLD) < 0 or int(WORLD) > 49:
        raise ValueError('Grid world input out of bound')
    string = './worlds/world' + str(WORLD) + '.txt'

    text_file = open(string, 'r')
    lines = text_file.readlines()
    maze = []
    for line in lines:
        line = line.strip().split(',')
        line = list(map(int, line))
        maze.append(line)

    SIZE = len(maze)
    pygame.init()
    screen = pygame.display.set_mode(((SIZE*8)+1,(SIZE*8)+1))
    #print(maze)

    quit = None
    while quit is None:
        for row in range(SIZE):
            for column in range(SIZE):
                color = BLACK
                if maze[row][column] == 0:
                    color = WHITE
                    pygame.draw.rect(screen, color,
                                [(MARGIN + WIDTH) * column + MARGIN, (MARGIN + HEIGHT) * row + MARGIN, WIDTH, HEIGHT])

                if maze[row][column] == 1:
                    color = BLACK
                    pygame.draw.rect(screen, color,
                                    [(MARGIN + WIDTH) * column + MARGIN, (MARGIN + HEIGHT) * row + MARGIN, WIDTH,
                                    HEIGHT])
                if maze[row][column] == 3:
                    color = RED
                    pygame.draw.rect(screen, color,
                                    [(MARGIN + WIDTH) * column + MARGIN, (MARGIN + HEIGHT) * row + MARGIN, WIDTH,
                                    HEIGHT])
                if maze[row][column] == 4:
                    color = GREEN
                    pygame.draw.rect(screen, color,
                                    [(MARGIN + WIDTH) * column + MARGIN, (MARGIN + HEIGHT) * row + MARGIN, WIDTH,
                                    HEIGHT])

        pygame.display.flip()

        if ASTAR == 1:
            if TIEBREAK == 1:
                wall, explored, path = repeat(maze)
            else:
                wall, explored, path = MaxRepeat(maze)
        elif ASTAR == 2:
            if TIEBREAK == 1:
                wall, explored, path = repeatBackwards(maze)
            else:
                wall, explored, path = maxRepeatBackwards(maze)
        else:
            if TIEBREAK == 1:
                wall, explored, path = repeatAdaptive(maze)
            else:
                wall, explored, path = MaxRepeatAdaptive(maze)


        # wall, explored, path = MaxRepeat(maze)
        # wall, explored, path = repeatBackwards(maze)
        # wall, explored, path = repeatAdaptive(maze)
        # wall, explored, path = MaxRepeatAdaptive(maze)
        # wall, explored, path = maxRepeatBackwards(maze)


        for cell in explored:
            color = BLUE
            pygame.draw.rect(screen, color,
                        [(MARGIN + WIDTH) * cell[1] + MARGIN, (MARGIN + HEIGHT) * cell[0] + MARGIN, WIDTH,
                        HEIGHT])
            pygame.display.flip()

        for cell in wall:
            color = GREEN
            pygame.draw.rect(screen, color,
                        [(MARGIN + WIDTH) * cell[1] + MARGIN, (MARGIN + HEIGHT) * cell[0] + MARGIN, WIDTH,
                        HEIGHT])
            pygame.display.flip()

        if path is not None:
            for cell in path:
                color = YELLOW
                pygame.draw.rect(screen, color,
                                [(MARGIN + WIDTH) * cell[1] + MARGIN, (MARGIN + HEIGHT) * cell[0] + MARGIN, WIDTH,
                                HEIGHT])
                pygame.display.flip()
            print(len(path))
        quit = input("Enter any key to quit\n")

def HiddenVisualize(ASTAR, TIEBREAK, WORLD):
    if int(WORLD) < 0 or int(WORLD) > 49:
        raise ValueError('Grid world input out of bound')
    string = './worlds/world' + str(WORLD) + '.txt'

    text_file = open(string, 'r')
    lines = text_file.readlines()
    maze = []
    for line in lines:
        line = line.strip().split(',')
        line = list(map(int, line))
        maze.append(line)

    SIZE = len(maze)
    #print(maze)

    if ASTAR == 1:
        if TIEBREAK == 1:
            wall, explored, path = repeat(maze)
        else:
            wall, explored, path = MaxRepeat(maze)
    elif ASTAR == 2:
        if TIEBREAK == 1:
            wall, explored, path = repeatBackwards(maze)
        else:
            wall, explored, path = maxRepeatBackwards(maze)
    else:
        if TIEBREAK == 1:
            wall, explored, path = repeatAdaptive(maze)
        else:
            wall, explored, path = MaxRepeatAdaptive(maze)


        
    