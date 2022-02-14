import numpy as np
from random import randrange, sample
from itertools import product
import sys

np.set_printoptions(threshold=sys.maxsize)

DEBUG = False

def mazeInit(rows=101, columns=101):
    """
    Initializes numpy matrix as gridworld
    """

    maze = np.zeros((rows, columns), int)
    return maze


def move(currentCoordinate, unvisited):
    """
    Randomly choose a direction to move in among current unvisited neighbors
    """

    possibleMoves = []
    current = list(currentCoordinate)
    mv1 = tuple([current[0] - 1, current[1]])
    mv2 = tuple([current[0] + 1, current[1]])
    mv3 = tuple([current[0], current[1] - 1])
    mv4 = tuple([current[0], current[1] + 1])

    if mv1 in unvisited: possibleMoves.append(mv1)
    if mv2 in unvisited: possibleMoves.append(mv2)
    if mv3 in unvisited: possibleMoves.append(mv3)
    if mv4 in unvisited: possibleMoves.append(mv4)

    if len(possibleMoves) == 0: return None
    else:
        return possibleMoves[randrange(len(possibleMoves))]

def addObstructions(maze):
    """
    Uses the algorithm described in the Assignment 1 writeup to generate obstructions in the gridworld.
    """

    bounds = np.shape(maze)
    stack = []
    unvisited = set()

    # Create set of cartesian product for all possible coordinate pairs
    for item in product(range(bounds[0]), range(bounds[1])): 
        unvisited.add(item)

    while len(unvisited) > 0:

        # Choose a random location in gridworld and push to stack
        coordinate = sample(unvisited, 1)[0]
        if DEBUG: print("Chose " + str(coordinate) + " as random location")
        stack.append(coordinate)
        unvisited.remove(coordinate)

        while len(stack) > 0:
            nextMove = move(coordinate, unvisited)
            if DEBUG: print("Next move is: " + str(nextMove))
            if nextMove is None: # No neighbors remaining, backtrack through stack
                coordinate = stack.pop()
            else:
                coordinate = nextMove
                stack.append(nextMove)
                unvisited.remove(nextMove)
                if randrange(10) < 3:
                    maze[coordinate[0]][coordinate[1]] = 1
                    if DEBUG: print(str(coordinate) + " is now obstructed")
                
def addAgentAndTarget(maze):
    """
    Randomly place agent and target in the world
    """
    bounds = np.shape(maze)
    # maze[randrange(bounds[0])][randrange(bounds[1])] = 3 # Agent

    # # Ensure target is never on top of agent
    # r1 = randrange(bounds[0])
    # r2 = randrange(bounds[1])
    # while maze[r1][r2] == 3:
    #     r1 = randrange(bounds[0])
    #     r2 = randrange(bounds[1])
    # maze[r1][r2] = 4

    maze[0][0] = 3 # Agent
    maze[bounds[0]-1][bounds[1]-1] = 4 # Target

def viewMaze(maze):
    print(maze)

def createMazes(amount=1, rows=101, cols=101):
    mazes = []
    for i in range(amount):
        m = mazeInit(rows, cols)
        addObstructions(m)
        addAgentAndTarget(m)
        mazes.append(m)
        fname = f"./worlds/world{i}.txt"
        np.savetxt(fname, mazes[i], delimiter=",", newline="\n", fmt="%i")
    return mazes

if __name__ == "__main__":
    mazes = createMazes(1, 7, 7)
    viewMaze(mazes[0])