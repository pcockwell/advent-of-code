def split_list_on_common_bit(string_list, index):
  bit_sum = 0
  contains_one = []
  contains_zero = []
  for line in string_list:
    bit_sum += int(line[index])
    if line[index] == "1":
      contains_one.append(line)
    else:
      contains_zero.append(line)

  if bit_sum >= len(string_list) / 2.0:
    return contains_one, contains_zero

  return contains_zero, contains_one

with open("data-1.txt", "r") as data_file:
  oxygen_rating_possibilities = list(data_file.readlines())
  carbon_dioxide_rating_possibilities = list(oxygen_rating_possibilities)

  cur_index = 0
  while len(oxygen_rating_possibilities) > 1:
    oxygen_rating_possibilities, _ = split_list_on_common_bit(oxygen_rating_possibilities, cur_index)
    cur_index += 1

  cur_index = 0
  while len(carbon_dioxide_rating_possibilities) > 1:
    _, carbon_dioxide_rating_possibilities = split_list_on_common_bit(carbon_dioxide_rating_possibilities, cur_index)
    cur_index += 1

oxygen_rating = int(oxygen_rating_possibilities[0], 2)
carbon_dioxide_rating = int(carbon_dioxide_rating_possibilities[0], 2)

life_support_rating = oxygen_rating * carbon_dioxide_rating
print(life_support_rating)
