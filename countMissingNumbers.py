# Create a function that takes a list of "mostly" numbers, counts the amount of missing numbers and returns their sum. Watch 
# out for strings!

# Examples

# count_missing_nums(["1", "3", "5", "7", "9"]) ➞ 4
# # 1+1+1+1

# count_missing_nums(["7", "3", "1", "9", "5"]) ➞ 4

# count_missing_nums(["1", "5", "B", "9", "z"]) ➞ 6

def count_missing_nums(lst):
	lst = sorted(map(int,filter(lambda x: x.isnumeric(),lst)))
	return sum([lst[i+1] - lst[i] - 1 for i in range(len(lst)-1)])

print(count_missing_nums(["1", "3", "5", "7", "9"])) # ➞ 4
# 1+1+1+1
print(count_missing_nums(["7", "3", "1", "9", "5"])) # ➞ 4
print(count_missing_nums(["1", "5", "B", "9", "z"])) # ➞ 6

# def sum_of_missing_nums(lst):
# 	lst = [int(i) for i in lst if i.isdigit()]
# 	return max(lst) - min(lst) + 1 - len(lst)

