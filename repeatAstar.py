
from heapq import *
from anytree import Node, RenderTree, findall, find
from random import random
import numpy as np
from Maze import *
import sys
np.set_printoptions(threshold=sys.maxsize)



# Modify start and goal locations
start = (0,0)
goal = (100,100)
bounds = (101,101)

def getSolution(root):
    target = find(root, lambda node: node.name == str(goal))
    SOLUTION = []
    while target is not None:
        SOLUTION.insert(0, tuple(map(int, target.name[1:-1].split(', '))))
        target = target.parent
    return SOLUTION

def viewTree(tree):
    for pre, fill, node in RenderTree(tree):
        print("%s%s" % (pre, node.name))

def checkWalls(currentPosition, maze, WALL):
    c1 = (currentPosition[0] + 1, currentPosition[1])
    c2 = (currentPosition[0] - 1, currentPosition[1])
    c3 = (currentPosition[0], currentPosition[1] + 1)
    c4 = (currentPosition[0], currentPosition[1] - 1)
    c = [c1, c2, c3, c4]
    for cell in c:
        try:
            if maze[cell[0]][cell[1]] == 1:
                WALL.add((cell[0], cell[1]))
        except:
            continue


def repeat(maze):
    SOLUTION = Node(str(start))
    parentNode = SOLUTION
    WALL = set()
    currentPosition = start
    checkWalls(currentPosition, maze, WALL)
    EXPLORED = []
    EXPAND = set()
    iterations = 0
    while currentPosition != goal:

        # Get path with current information about walls from WALL
        CLOSED, PATH = Astar(currentPosition, maze, WALL)

        if PATH is None: 
            print(f"No path found after {iterations} iterations")
            return WALL ,EXPLORED, None

        # Follow path until we hit a wall while recording walls seen
        for expanded_coord in CLOSED:
          EXPAND.add(expanded_coord)
        for cell in PATH[1:]:
            if cell in WALL:
                break
            else:
                # Insert into tree the next move as a child of current move
                # If the parent of a node already exists, add child to existing node instead to allow for backtracking
                temp = findall(SOLUTION, lambda node: node.name == str(currentPosition))[0]

                if temp is not None:
                    parentNode = temp
                else:
                    parentNode = currentPosition

                Node(str(cell), parent=parentNode)
                EXPLORED.append(currentPosition)
                currentPosition = cell
                checkWalls(currentPosition, maze, WALL)
            break
        iterations += 1
    expandCount = len(EXPAND)
    print(f"Reached the target in {iterations} iterations")
    print(f"Reached the target in {expandCount} expansions")
    return WALL,  EXPLORED, getSolution(SOLUTION)
        # Find path with current information
        # Walk along path and record walls seen and recalculate if path goes through wall

def Astar(currentPosition, maze, WALL):
  """
  We represent each cell, containing a F value, G value, random value, X coordinate, Y coordinate, and Parent's coordinate, as a 6 value tuple.
  The starting cell and all examined neighbor cells are pushed into the OPEN list.
  When our agent visits a cell, that cell will be added into the CLOSED set.
  Neighbors explored will also be added into the CLOSED set to avoid backtracking.
  That cell's coordinate key will also be used to added its parent's value into a PATH dictionary. PATH will keep track of the correct pathing from start to goal. 

  H is the heuristic function used. In this case the Manhattan distance.
  G values are calculated for each cell in the open list as its manhattan distance relative to the agent's current location.
  F values is calculated by each cell manhattan distance relative to the goal.

  TIEBREAKING is done using minimal value of G. By documentation of Heapq, tiebreaking is implemented when using tuples. 
"""
  iterations = 0
  OPEN = []
  CLOSED = set()
  PATH = dict()

  # Initialize start cell
  g = 0
  h = manhattanDistance(start, goal)
  f = g + h
  # f value, g value, x, y, parent (x, y)
  heappush(OPEN, (f, g, random(), currentPosition[0], currentPosition[1],None)) 
  
  while len(OPEN) > 0:
    current = heappop(OPEN)
    if current is not None:
      current_coord = (current[3],current[4])

    if current_coord in CLOSED:
      continue
    # Add current into closed list to avoid revisiting them.      
    CLOSED.add((current[3], current[4]))
    PATH[(current[3], current[4])] = current[5]
    # Reached the goal?
    if current[3] == goal[0] and current[4] == goal[1]:
        return CLOSED, getPath(PATH,goal)

    examineNeighbors(current, maze, goal, CLOSED, OPEN, PATH, WALL)
    
    iterations += 1
  return CLOSED, None

# Heuristic Function
def manhattanDistance(current, goal):
	return abs(current[0] - goal[0]) + abs(current[1] - goal[1])

def examineNeighbors(current, maze, goal, CLOSED, OPEN, PATH, WALL):
  """
  View cells immediately to the right, left, top, and bottom of the agent and determine if they are valid moves. For each neighboring cell, calculate a tuple set and insert them into OPEN heap for consideration as future moves.
  """
  
  # View all four neighbors
  coords = []
  c1 = (current[3] + 1, current[4])
  c2 = (current[3] - 1, current[4])
  c3 = (current[3], current[4] + 1)
  c4 = (current[3], current[4] - 1)
  c = [c1, c2, c3, c4]
    
  # Check if neighbors are valid moves
  for i in range(len(c)):
    x = c[i][0]
    y = c[i][1]
    if x >= 0 and x <= bounds[0] - 1 and y >= 0 and y <= bounds[1] - 1 and (x,y) not in WALL:
      coords.append(c[i])
  
  for neighbor in coords:    
    if neighbor not in CLOSED:      
    # Calculate tuple set
      current_coord = (current[3],current[4])
      g = current[1] + manhattanDistance(neighbor, current_coord )
      f = g + manhattanDistance(neighbor, goal)
      neighborTuple = (f,g,random(),neighbor[0],neighbor[1],(current[3],current[4]))
      heappush(OPEN, neighborTuple)
      PATH[(neighbor[0], neighbor[1])] = (current[3], current[4])
 
def getPath(PATH, goal):
  """
  Helper function to retreive the correct pathing from start to goal from the PATH dictionary.
  """
  current = goal
  result = [goal]
  while(current is not None):
    current = (PATH.get(current))
    if current is not None:
      result.insert(0, current)
  return result


if __name__ == "__main__":
#   x = [
#   [0, 0, 0, 0, 0],
#   [0, 0, 1, 0, 0],
#   [0, 0, 1, 1, 0],
#   [0, 0, 1, 1, 0],
#   [0, 0, 3, 1, 4]]
#   x = [
#   [3, 0, 0, 0, 0],
#   [0, 1, 0, 0, 0],
#   [0, 1, 0, 0, 0],
#   [0, 1, 1, 1, 1],
#   [0, 0, 0, 0, 4]]

  # x = [
  # [3, 0, 0, 0, 0],
  # [0, 0, 0, 0, 0],
  # [0, 0, 0, 0, 0],
  # [0, 0, 0, 0, 0],
  # [0, 0, 0, 0, 4]]
#   mazes = np.array(x)
  mazes = createMazes(1, 6, 6)
  viewMaze(mazes[0])
  repeat(mazes[0])