from pprint import pprint
from collections import defaultdict

def show_graph(graph):
  for y_tile_idx in range(5):
    for y, row in enumerate(graph):
      for x_tile_idx in range(5):
        for x, risk in enumerate(row):
          print(get_location_risk(graph, x_tile_idx * len(graph[0]) + x, y_tile_idx * len(graph) + y), end='')
      print()

def get_location_risk(graph, x, y):
  tile_x = int(x / len(graph[0]))
  graph_x = x % len(graph[0])
  tile_y = int(y / len(graph))
  graph_y = y % len(graph)
  risk = (tile_x + tile_y + graph[graph_y][graph_x])
  if risk > 9:
    risk = risk % 9
  return risk

def find_lowest_risk_path(graph, paths_by_risk):
  visited = {}
  while paths_by_risk:
    lowest_risk = min(paths_by_risk.keys())
    x, y = paths_by_risk[lowest_risk].pop(0)
    if len(paths_by_risk[lowest_risk]) == 0:
      del paths_by_risk[lowest_risk]

    if (x, y) in visited and visited[(x, y)] <= lowest_risk:
      continue

    visited[(x, y)] = lowest_risk

    if x == (len(graph[0]) * 5) - 1 and y == (len(graph) * 5) - 1:
      return lowest_risk

    if x < (len(graph[0]) * 5) - 1:
      right_node_risk = get_location_risk(graph, x + 1, y)
      # print(lowest_risk + right_node_risk, (x + 1, y))
      paths_by_risk[lowest_risk + right_node_risk].append((x + 1, y))

    if x > 0:
      left_node_risk = get_location_risk(graph, x - 1, y)
      # print(lowest_risk + right_node_risk, (x + 1, y))
      paths_by_risk[lowest_risk + left_node_risk].append((x - 1, y))

    if y < (len(graph) * 5) - 1:
      below_node_risk = get_location_risk(graph, x, y + 1)
      # print(lowest_risk + below_node_risk, (x, y + 1))
      paths_by_risk[lowest_risk + below_node_risk].append((x, y + 1))

    if y > 0:
      above_node_risk = get_location_risk(graph, x, y - 1)
      # print(lowest_risk + below_node_risk, (x, y + 1))
      paths_by_risk[lowest_risk + above_node_risk].append((x, y - 1))

graph = []
with open("data-1.txt", "r") as data_file:
  for line in data_file.readlines():
    graph.append([int(risk) for risk in line.strip()])

# show_graph(graph)

paths_by_risk = defaultdict(list)

x_pos, y_pos = 0, 0
paths_by_risk[0].append((x_pos, y_pos))

shortest_path_risk = find_lowest_risk_path(graph, paths_by_risk)
print(shortest_path_risk)
