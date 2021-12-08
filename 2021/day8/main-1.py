count_one_four_seven_eight = 0
with open("data-1.txt", "r") as data_file:
  for line in data_file.readlines():
    signal_patterns, output_values = line.split(' | ')
    for value in output_values.split():
      if len(value) in [2, 3, 4, 7]:
        count_one_four_seven_eight += 1

print(count_one_four_seven_eight)
