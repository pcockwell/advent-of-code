num_increases = 0
last_num = None
with open("data-1.txt", "r") as data_file:
  for line in data_file.readlines():
    current_num = int(line)
    if last_num and current_num > last_num:
      num_increases += 1
    last_num = current_num

print(num_increases)
