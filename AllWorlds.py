from Visualization import HiddenVisualize

for i in range(1,4):
  for j in range(1, 3):
    for k in range(2):
      HiddenVisualize(i, j, k)
      print(f"Running astar mode {i} with tiebreak {j} on world {k}")
    print(f"50 worlds done for astar {i} on tiebreak {j}\n\n")
  print(f"Tiebreak done for astar {i}")
print("Astars done")
