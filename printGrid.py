# Write a method that accepts two integer parameters rows and cols. The output is a 2d array of numbers displayed in 
# column-major order, meaning the numbers shown increase sequentially down each column and wrap to the top of the next 
# column to the right once the bottom of the current column is reached.

# Examples

# printgrid(3, 6) ➞ [
#   [1, 4, 7, 10, 13, 16],
#   [2, 5, 8, 11, 14, 17],
#   [3, 6, 9, 12, 15, 18]
# ]

# printgrid(5, 3) ➞ [
#   [1, 6, 11],
#   [2, 7, 12],
#   [3, 8, 13],
#   [4, 9, 14],
#   [5, 10, 15]
# ]

# printgrid(4, 1) ➞ [
#   [1],
#   [2],
#   [3],
#   [4]
# ]

def printgrid(rows, cols):
    return [[j for j in range(i+1,rows*cols+1,rows)] for i in range(rows)]


print(printgrid(3, 6)) # ➞ [
#   [1, 4, 7, 10, 13, 16],
#   [2, 5, 8, 11, 14, 17],
#   [3, 6, 9, 12, 15, 18]
# ]

print(printgrid(5, 3)) # ➞ [
# #   [1, 6, 11],
# #   [2, 7, 12],
# #   [3, 8, 13],
# #   [4, 9, 14],
# #   [5, 10, 15]
# # ]

print(printgrid(4, 1)) # ➞ [
# #   [1],
# #   [2],
# #   [3],
# #   [4]
# # ]

# def printgrid(r, c):
# 	return [[1 + i + j*r for j in range(c)] for i in range(r)]

# def printgrid(rows, cols):
#     return [list(range(i, rows*cols+1, rows)) for i in range(1, rows+1)]

