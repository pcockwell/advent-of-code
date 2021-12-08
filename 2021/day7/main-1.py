with open("data-1.txt", "r") as data_file:
  positions = [int(n) for n in data_file.readline().split(',')]
  max_pos = None
  min_pos = None
  for pos in positions:
    if max_pos is None or pos > max_pos:
      max_pos = pos
    if min_pos is None or pos < min_pos:
      min_pos = pos

  min_fuel_usage = None
  for reference_pos in range(min_pos, max_pos + 1):
    fuel_usage = 0
    for pos in positions:
      fuel_usage += abs(reference_pos - pos)

    if min_fuel_usage is None or fuel_usage < min_fuel_usage:
      min_fuel_usage = fuel_usage

print(min_fuel_usage)
