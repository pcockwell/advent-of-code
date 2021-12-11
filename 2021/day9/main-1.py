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

def risk_score(height_map, row, col):
  return int(height_map[row][col]) + 1

sum_of_risk_scores = 0
height_map = []
with open("data-1.txt", "r") as data_file:
  for line in data_file.readlines():
    height_map.append(list(line.strip()))

for row in range(len(height_map)):
  for col in range(len(height_map[row])):
    if is_low_point(height_map, row, col):
      sum_of_risk_scores += risk_score(height_map, row, col)

print(sum_of_risk_scores)
