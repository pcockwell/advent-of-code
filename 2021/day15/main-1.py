from pprint import pprint
from collections import defaultdict

def find_lowest_risk_path(graph, paths_by_risk):
  visited = []
  while paths_by_risk:
    lowest_risk = min(paths_by_risk.keys())
    x, y = paths_by_risk[lowest_risk].pop(0)
    if len(paths_by_risk[lowest_risk]) == 0:
      del paths_by_risk[lowest_risk]

    if (x, y) in visited:
      continue

    visited.append((x, y))

    if x == len(graph[0]) - 1 and y == len(graph) - 1:
      return lowest_risk

    if x < len(graph[0]) - 1:
      right_node_risk = graph[y][x + 1]
      paths_by_risk[lowest_risk + right_node_risk].append((x + 1, y))

    if y < len(graph) - 1:
      below_node_risk = graph[y + 1][x]
      paths_by_risk[lowest_risk + below_node_risk].append((x, y + 1))

graph = []
with open("data-1.txt", "r") as data_file:
  for line in data_file.readlines():
    graph.append([int(risk) for risk in line.strip()])

paths_by_risk = defaultdict(list)

x_pos, y_pos = 0, 0
paths_by_risk[0].append((x_pos, y_pos))

shortest_path_risk = find_lowest_risk_path(graph, paths_by_risk)
print(shortest_path_risk)
