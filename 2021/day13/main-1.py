from pprint import pprint

def display(grid, max_x, max_y):
  print('-' * 20)
  for y in range(max_y + 1):
    row = []
    for x in range(max_x + 1):
      if y in grid and x in grid[y]:
        row.append('#')
      else:
        row.append('.')
    print(' '.join(row))
  print('-' * 20)

def make_fold(grid, direction, location):
  new_grid = {}
  max_x = None
  max_y = None

  if direction == 'x':
    for y in grid:
      new_grid[y] = {}
      if max_y is None or y > max_y:
        max_y = y

      for x in grid[y]:
        new_x = x
        if x > location:
          new_x = location - abs(x - location)

        if max_x is None or new_x > max_x:
          max_x = new_x

        new_grid[y][new_x] = 1

  elif direction == 'y':
    for y in grid:
      new_y = y
      if y > location:
        new_y = location - abs(y - location)

      if new_y not in new_grid:
        new_grid[new_y] = {}

      if max_y is None or new_y > max_y:
        max_y = new_y

      for x in grid[y]:
        if max_x is None or x > max_x:
          max_x = x

        new_grid[new_y][x] = 1

  return new_grid, max_x, max_y

def num_points(grid):
  points = 0
  for _, row in grid.items():
    points += sum(row.values())
  return points

grid = {}
fold_instructions = []
still_adding_points = True

max_x = None
max_y = None
with open("data-1.txt", "r") as data_file:
  for line in data_file.readlines():
    if still_adding_points:
      if line == '\n':
        still_adding_points = False
        continue

      x, y = line.strip().split(',')
      x = int(x)
      y = int(y)
      if y not in grid:
        grid[y] = {}
      grid[y][x] = 1

      if max_x is None or x > max_x:
        max_x = x
      if max_y is None or y > max_y:
        max_y = y

    else:
      direction, location = line.strip().split(' ')[-1].split('=')
      fold_instructions.append((direction, int(location)))

# display(grid, max_x, max_y)
# print(num_points(grid))
pprint(fold_instructions)
for direction, location in fold_instructions:
  grid, max_x, max_y = make_fold(grid, direction, location)
  # display(grid, max_x, max_y)
  print(num_points(grid))


