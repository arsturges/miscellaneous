import numpy as np
import matplotlib.pyplot as plt
all_possible_products = []
for i in range(10):
  for j in range(10):
    for k in range(10):
      all_possible_products.append(i*j*k)

n, bins, patches = plt.hist(all_possible_products, 50)
#plt.show() # This shows that most common is zero, by far
# Confirm this:
product_counts = {}
for product in all_possible_products:
  if product in product_counts.keys():
    product_counts[product] += 1
  else:
    product_counts[product] = 1

num_products = len(product_counts.values())
target_product_count = np.sort(product_counts.values())[num_products-2:num_products-1]
assert target_product_count == 24
# So the product we're looking for is 72.
# Find all triplets of 72 where each component is less than 10.

factors_of_72_less_than_10 = []
for i in range(1,73): # [1,2,3 ... 70,71,72]
  if 72 % i == 0:
    if i < 10:
      factors_of_72_less_than_10.append(i)
factors = factors_of_72_less_than_10

all_possible_combinations = []
for i in factors:
  for j in factors:
    for k in factors:
      if i*j*k == 72:
        all_possible_combinations.append([i,j,k])

"""
Assuming lock starts in position {1,2,3}, what sequence of moves can you make
in order to try every possible valid combination in the minimum number of moves?
There are 1000 possible combinations, so minumum number of moves is 1000. 

Moving from {1,2,3} to {1,2,4} is one 'move'; moving from {9,9,9} to {0,0,0} 
is three 'moves'.

First try going straight down the list; count each move.
"""


def combo_moves(start_combo, end_combo):
  """
  A function that takes two combos and returns the number of moves needed to get
  from one to the second. Assume we take shortest route around the wheel (i.e.
  go from 9 directly to 0, not 9 to 8 to 7...to 2 to 1.
  """
  assert type(start_combo)==list
  assert len(start_combo)==3
  assert type(end_combo)==list
  assert len(end_combo)==3
  wheel_moves = {0:0, 1:1, 2:2, 3:3, 4:4, 5:5, 6:4, 7:3, 8:2, 9:1}
  total_moves = 0
  for wheel_number in [0,1,2]:
    difference = abs(end_combo[wheel_number] - start_combo[wheel_number])
    total_moves += wheel_moves[difference]
  return total_moves

assert combo_moves([0,0,0],[1,1,1]) == 3
assert combo_moves([0,0,0],[9,9,9]) == 3
assert combo_moves([3,4,5],[8,1,4]) == (5+3+1)

# Add initial combo to top of all_possible_combinations:
all_possible_combinations = [[1,2,3]] + all_possible_combinations
total_moves = 0

combos = all_possible_combinations # shorten name
for combo in range((len(combos)-1)):
  total_moves += combo_moves(combos[combo], combos[combo+1])
  
# Stack it up properly to start at {1,2,3}:
bottom_half = all_possible_combinations[:123]
top_half = all_possible_combinations[123:1000]
combo_stack = top_half + bottom_half
total_moves = 0
wheel1_start = 1
wheel2_start = 2
wheel3_start = 3
for combination in combo_stack:
  wheel1_end = combo[0]
  wheel2_end = combo[1]
  wheel3_end = combo[2]
  wheel1_movement = abs(wheel1_end - wheel1_start)
