from pprint import pprint

def apply_insertion_rules(polymer, insertion_rules):
  new_polymer = ''
  for char_idx in range(len(polymer)):
    new_polymer += polymer[char_idx]
    if char_idx < len(polymer) - 1:
      key = polymer[char_idx:char_idx + 2]
      if key in insertion_rules:
        new_polymer += insertion_rules[key]

  return new_polymer

def count_elements(polymer):
  element_count = {}
  for element in polymer:
    element_count[element] = element_count.get(element, 0) + 1

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
    insertion_rules[key] = val

polymer = starting_polymer
for i in range(10):
  polymer = apply_insertion_rules(polymer, insertion_rules)

element_count = count_elements(polymer)
print(element_count)
print(max(element_count.values()) - min(element_count.values()))
