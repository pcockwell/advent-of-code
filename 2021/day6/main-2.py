def process_spawning_for_day(old_fish_age_counts):
  new_fish_age_counts = {}

  for age in range(9):
    old_fish_at_age = 0
    if age in old_fish_age_counts:
      old_fish_at_age = old_fish_age_counts[age]

    if age == 0:
      new_fish_age_counts[6] = old_fish_at_age
      new_fish_age_counts[8] = old_fish_at_age
    else:
      if age - 1 not in new_fish_age_counts:
        new_fish_age_counts[age - 1] = 0
      new_fish_age_counts[age - 1] += old_fish_at_age

  return new_fish_age_counts

fish_age_counts = {}
with open("data-1.txt", "r") as data_file:
  fish_ages = [int(n) for n in data_file.readline().split(',')]
  for age in fish_ages:
    if age not in fish_age_counts:
      fish_age_counts[age] = 0

    fish_age_counts[age] += 1

  for i in range(256):
    fish_age_counts = process_spawning_for_day(fish_age_counts)

  print(sum(fish_age_counts.values()))
