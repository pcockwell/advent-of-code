from pprint import pprint

def apply_insertion_rules(polymer_pairs, insertion_rules):
  new_polymer_pairs = {}
  for pair, count in polymer_pairs.items():
    if pair in insertion_rules:
      for new_pair in insertion_rules[pair]:
        new_polymer_pairs[new_pair] = new_polymer_pairs.get(new_pair, 0) + count

  return new_polymer_pairs

def count_elements(polymer_pairs, last_element):
  element_count = {}
  for pair, count in polymer_pairs.items():
    element_count[pair[0]] = element_count.get(pair[0], 0) + count

  element_count[last_element] = element_count.get(last_element, 0) + 1

  return element_count

insertion_rules = {}
with open("data-1.txt", "r") as data_file:
  # Get initial polymer
  starting_polymer = data_file.readline().strip()

  # Skip empty line
  data_file.readline()

  # Parse insertion rules
  for line in data_file.readlines():
    key, val = line.strip().split(' -> ')
    insertion_rules[key] = (key[0] + val, val + key[1])

polymer_pairs = {}
for char_idx in range(len(starting_polymer) - 1):
  key = starting_polymer[char_idx:char_idx + 2]
  polymer_pairs[key] = polymer_pairs.get(key, 0) + 1

last_element = starting_polymer[-1]
for i in range(40):
  # pprint(polymer_pairs)
  polymer_pairs = apply_insertion_rules(polymer_pairs, insertion_rules)

element_count = count_elements(polymer_pairs, last_element)
print(element_count)
print(max(element_count.values()) - min(element_count.values()))
