"""Given a number, return the difference between the maximum and minimum numbers that can be formed when the digits are rearranged.
Examples

rearranged_difference(972882) ➞ 760833
# 988722 - 227889 = 760833

rearranged_difference(3320707) ➞ 7709823
# 7733200 - 23377 = 7709823

rearranged_difference(90010) ➞ 90981
# 91000 - 19 = 90981"""

def rearranged_difference(num):
    numSortMin = int("".join(sorted(str(num))))
    numSortMax = int("".join(sorted(str(num), reverse=True)))
    return numSortMax - numSortMin

print(rearranged_difference(972882))
print(rearranged_difference(3320707))
print(rearranged_difference(90010))

def rearranged_difference(num):
    return int("".join(sorted(str(num),reverse=True)))-int("".join(sorted(str(num))))

print(rearranged_difference(972882))
print(rearranged_difference(3320707))
print(rearranged_difference(90010))

"""def rearranged_difference(num):
	n = ''.join(sorted(str(num)))
	return int(n[::-1]) - int(n)"""


