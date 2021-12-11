def is_low_point(height_map, row, col):
  current_val = int(height_map[row][col])

  if row > 0 and int(height_map[row - 1][col]) <= current_val:
      return False

  if row < len(height_map) - 1 and int(height_map[row + 1][col]) <= current_val:
      return False

  if col > 0 and int(height_map[row][col - 1]) <= current_val:
      return False

  if col < len(height_map[row]) - 1 and int(height_map[row][col + 1]) <= current_val:
      return False

  return True

def basin_size(height_map, row, col):
  locations_in_basin = [(row, col)]
  current_location_index = 0

  while current_location_index < len(locations_in_basin):
    cur_row, cur_col = locations_in_basin[current_location_index]
    for x, y in [
      (-1, 0),
      (1, 0),
      (0, -1),
      (0, 1)
    ]:
      if (
        cur_row + y >= 0 and
        cur_row + y < len(height_map) and
        cur_col + x >= 0 and
        cur_col + x < len(height_map[cur_row + y])
      ) and \
      int(height_map[cur_row + y][cur_col + x]) < 9 and \
      (cur_row + y, cur_col + x) not in locations_in_basin:
        locations_in_basin.append((cur_row + y, cur_col + x))

    current_location_index += 1

  return len(locations_in_basin)


basin_sizes = []
height_map = []
with open("data-1.txt", "r") as data_file:
  for line in data_file.readlines():
    height_map.append(list(line.strip()))

for row in range(len(height_map)):
  for col in range(len(height_map[row])):
    if is_low_point(height_map, row, col):
      basin_sizes.append(basin_size(height_map, row, col))

print(basin_sizes)
top_3_basin_sizes = sorted(basin_sizes, reverse=True)[0:3]
print(top_3_basin_sizes)
result = 1
for size in top_3_basin_sizes:
  result = result * size

print(result)
