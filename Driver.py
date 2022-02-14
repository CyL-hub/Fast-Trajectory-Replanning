from Visualization import visualize

if __name__ == "__main__":
  print("Enter 1 for Repeated Forwards A*")
  print("Enter 2 for Repeated Backwards A*")
  print("Enter 3 for Adaptive A*")
  ASTAR = int(input("Choose which A* to perform:\n"))
  print("Enter 1 to tie break on small g")
  print("Enter 2 to tiebreak on large g")
  TIEBREAK = int(input("Choose how to tiebreak:\n"))
  WORLD = int(input("Choose a world to search on from 0 to 49:\n"))

  if ASTAR > 3 or ASTAR < 1:
    raise ValueError('A* selection invalid')
  elif TIEBREAK > 2 or TIEBREAK < 1:
    raise ValueError('Tiebreak selection invalid')
  elif WORLD < 0 or WORLD > 49:
    raise ValueError('World selection invalid')

  visualize(ASTAR, TIEBREAK, WORLD)
  