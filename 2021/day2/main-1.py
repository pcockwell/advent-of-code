horizontal_position = 0
depth = 0
with open("data-1.txt", "r") as data_file:
  for line in data_file.readlines():
    command, distance = line.split()
    if command == 'forward':
      horizontal_position += int(distance)
    elif command == 'down':
      depth += int(distance)
    elif command == 'up':
      depth -= int(distance)

print(horizontal_position * depth)
