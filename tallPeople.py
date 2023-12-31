# Create a function that takes a 2D array as an argument and returns the number of people whose view is blocked by a tall person. 
# The concert stage is pointed towards the top of the 2D array and the tall person (represented by a 2) blocks the view of all the 
# people (represented by a 1) behind them.

# Examples

# block([
#   [1, 1, 1, 1, 1],
#   [1, 1, 1, 1, 1],
#   [1, 1, 1, 1, 2],
#   [1, 1, 1, 1, 1],
#   [1, 1, 1, 1, 1]
# ]) ➞ 2

# # The tall person blocks 2 people behind him thus
# # the function returns 2.


# block([
#   [1, 2, 1, 1],
#   [1, 1, 1, 2],
#   [1, 1, 1, 1],
#   [1, 1, 1, 1],
# ]) ➞ 5

# # There are 2 tall people that block everyone behind
# # them. The first tall person in the first row blocks 3
# # people behind him while the second tall person in
# # the second row blocks 2 people behind him thus the
# # function returns 5.


# block([
#   [1, 1, 1, 1],
#   [2, 1, 1, 2],
#   [1, 1, 1, 1],
#   [1, 1, 1, 1],
# ]) ➞ 4

# Notes

#     There is only a maximum of 1 tall person in every column.
#     No view is blocked if the tall person is in the last row.

def block(lst):
    return sum(j for i in (i[i.index(2)+1:] for i in zip(*lst) if 2 in i) for j in i)

print(block([
  [1, 1, 1, 1, 1],
  [1, 1, 1, 1, 1],
  [1, 1, 1, 1, 2],
  [1, 1, 1, 1, 1],
  [1, 1, 1, 1, 1]
])) # ➞ 2

print(block([
  [1, 2, 1, 1],
  [1, 1, 1, 2],
  [1, 1, 1, 1],
  [1, 1, 1, 1],
])) # ➞ 5

print(block([
  [1, 1, 1, 1],
  [2, 1, 1, 2],
  [1, 1, 1, 1],
  [1, 1, 1, 1],
])) # ➞ 4

# def block(lst):
# 	return sum(len(i) - i.index(2) - 1 for i in zip(*lst) if 2 in i)

# def block(lst):
# 	return sum(l.count(2)*(len(lst)-i-1) for i,l in enumerate(lst))
