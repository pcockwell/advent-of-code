def line_coordinates(line):
  start, end = line.split(' -> ')
  start_x, start_y = start.split(',')
  start_x, start_y = int(start_x), int(start_y)
  end_x, end_y = end.split(',')
  end_x, end_y = int(end_x), int(end_y)

  if start_x == end_x:
    for y_val in range(min(start_y, end_y), max(start_y, end_y)+1):
      yield (start_x, y_val)

  elif start_y == end_y:
    for x_val in range(min(start_x, end_x), max(start_x, end_x)+1):
      yield (x_val, start_y)

num_dangerous_squares = 0
vent_map = {}
max_x = None
max_y = None
with open("data-1.txt", "r") as data_file:
  for line in data_file.readlines():
    for xcoord, ycoord in line_coordinates(line):
      if not max_x or xcoord > max_x:
        max_x = xcoord
      if not max_y or xcoord > max_y:
        max_y = ycoord

      if ycoord not in vent_map:
        vent_map[ycoord] = {}

      if xcoord not in vent_map[ycoord]:
        vent_map[ycoord][xcoord] = 0

      vent_map[ycoord][xcoord] += 1

  for row in vent_map.values():
    for count in row.values():
      if count > 1:
        num_dangerous_squares += 1

print(num_dangerous_squares)
