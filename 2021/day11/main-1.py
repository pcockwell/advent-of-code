from pprint import pprint

def count_flashes_for_one_step(grid):
  flashed = []
  for row in range(10):
    for col in range(10):
      grid[row][col] += 1
      if grid[row][col] > 9:
        flashed.append((row, col))

  cur_index = 0
  while cur_index < len(flashed):
    row, col = flashed[cur_index]
    for x, y in [
      (-1, -1),
      (-1, 0),
      (-1, 1),
      (0, -1),
      (0, 1),
      (1, -1),
      (1, 0),
      (1, 1),
    ]:
      if (
        row + y >= 0 and
        row + y < 10 and
        col + x >= 0 and
        col + x < 10
      ):
        grid[row + y][col + x] += 1
        if int(grid[row + y][col + x]) > 9 and (row + y, col + x) not in flashed:
          flashed.append((row + y, col + x))

    cur_index += 1

  for row, col in flashed:
    grid[row][col] = 0

  # pprint(flashed)
  return len(flashed)

num_flashes = 0
grid = []
with open("data-1.txt", "r") as data_file:
  for line in data_file.readlines():
    grid.append([int(c) for c in line.strip()])

for step in range(100):
  # print("Step " + str(step))
  # pprint(grid)
  num_flashes += count_flashes_for_one_step(grid)

print(num_flashes)
