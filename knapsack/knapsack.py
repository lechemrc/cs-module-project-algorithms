#!/usr/bin/python

import sys
# from collections import namedtuple

# Item = namedtuple('Item', ['index', 'size', 'value'])

# def knapsack_solver(items, weight_limit):
#     max_value = -1
#     best_combo = None
#     for i in range(1, len(items)+1):
#         list_of_combos = list(combinations(items, i))
#         for combo in list_of_combos:
#             value = 0 # of the entire combo
#             weight = 0 # of the entire combo
#             for item in combo:
#                 value += item.value
#                 weight += item.weight
#             if weight <= weight_limit:
#                 if value > max_value:
#                     max_value = value
#                     best_combo = combo

#     return best_combo


if __name__ == '__main__':
  if len(sys.argv) > 1:
    capacity = int(sys.argv[2])
    file_location = sys.argv[1].strip()
    file_contents = open(file_location, 'r')
    items = []

    for line in file_contents.readlines():
      data = line.rstrip().split()
      items.append(Item(int(data[0]), int(data[1]), int(data[2])))
    
    file_contents.close()
    print(knapsack_solver(items, capacity))
  else:
    print('Usage: knapsack.py [filename] [capacity]')
