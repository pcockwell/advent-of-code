def process_spawning_for_day(all_fish):
  new_state_of_old_fish = []
  new_fish = []

  for fish in all_fish:
    if fish == 0:
      new_state_of_old_fish.append(6)
      new_fish.append(8)
    else:
      new_state_of_old_fish.append(fish - 1)

  return new_state_of_old_fish + new_fish

with open("data-1.txt", "r") as data_file:
  fish = [int(n) for n in data_file.readline().split(',')]
  for i in range(80):
    fish = process_spawning_for_day(fish)

  print(len(fish))
