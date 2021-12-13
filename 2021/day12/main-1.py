from pprint import pprint


class Cave:
  SIZE_LARGE = 'large'
  SIZE_SMALL = 'small'

  def __init__(self, label):
    self.label = label
    if self.label.islower():
      self.size = self.SIZE_SMALL
    else:
      self.size = self.SIZE_LARGE
    self.linked_caves = []

  def is_small(self):
    return self.size == 'small'

  def add_linked_cave(self, cave):
    if cave not in self.linked_caves:
      self.linked_caves.append(cave)
      return True

    return False


def find_paths(all_caves, path_so_far):
  paths = set()

  if type(path_so_far) != list:
    path_so_far = [path_so_far]

  current_cave = all_caves[path_so_far[-1]]
  for new_cave in current_cave.linked_caves:
    if new_cave.label in path_so_far and new_cave.is_small():
      continue
    elif new_cave.label == "end":
      solution_path = ','.join(path_so_far + [new_cave.label])
      paths.add(solution_path)
    else:
      new_paths = find_paths(all_caves, path_so_far + [new_cave.label])
      paths.update(new_paths)

  return paths

all_caves = {}
with open("data-1.txt", "r") as data_file:
  for line in data_file.readlines():
    cave1, cave2 = line.strip().split('-')
    if cave1 not in all_caves:
      all_caves[cave1] = Cave(cave1)
    if cave2 not in all_caves:
      all_caves[cave2] = Cave(cave2)

    all_caves[cave1].add_linked_cave(all_caves[cave2])
    all_caves[cave2].add_linked_cave(all_caves[cave1])

paths = find_paths(all_caves, ['start'])
# print(paths)
print(len(paths))
