# Write a function that sorts the positive numbers in ascending order, and keeps the negative numbers untouched.
# Examples

# pos_neg_sort([6, 3, -2, 5, -8, 2, -2]) ➞ [2, 3, -2, 5, -8, 6, -2]

# pos_neg_sort([6, 5, 4, -1, 3, 2, -1, 1]) ➞ [1, 2, 3, -1, 4, 5, -1, 6]

# pos_neg_sort([-5, -5, -5, -5, 7, -5]) ➞ [-5, -5, -5, -5, 7, -5]

# pos_neg_sort([]) ➞ []

# Notes

#     If given an empty list, you should return an empty list.
#     Integers will always be either positive or negative (0 isn't included in the tests).

def pos_neg_sort(lst):
    pos = sorted(i for i in lst if i>0)
    s = []
    for i in lst:
        if i > 0:
            s.append(pos[0])
            del pos[0]
        else:
            s.append(i)
    return s
    
print(pos_neg_sort([6, 3, -2, 5, -8, 2, -2])) # ➞ [2, 3, -2, 5, -8, 6, -2]
print(pos_neg_sort([6, 5, 4, -1, 3, 2, -1, 1])) # ➞ [1, 2, 3, -1, 4, 5, -1, 6]
print(pos_neg_sort([-5, -5, -5, -5, 7, -5])) # ➞ [-5, -5, -5, -5, 7, -5]
print(pos_neg_sort([])) # ➞ []

# def pos_neg_sort(l):
#   pos = sorted( n for n in l if n>0 )
#   return [ pos.pop(0) if n>0 else n for n in l ]

# def pos_neg_sort(lst):
#     pos = sorted(x for x in lst if x > 0)[::-1]
#     return [pos.pop() if i > 0 else i for i in lst]