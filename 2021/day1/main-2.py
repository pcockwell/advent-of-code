num_increases = 0
number_window = []
with open("data-1.txt", "r") as data_file:
  for line in data_file.readlines():
    number = int(line)
    last_sum = None
    if len(number_window) == 3:
      last_sum = sum(number_window)
      number_window.pop(0)
    number_window.append(number)
    current_sum = sum(number_window)
    if last_sum and current_sum > last_sum:
      num_increases += 1

print(num_increases)
