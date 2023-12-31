"""Create a function that takes a string containing integers as well as other characters and return the sum of the negative integers only.
Examples

negative_sum("-12 13%14&-11") ➞ -23
# -12 + -11 = -23

negative_sum("22 13%14&-11-22 13 12") ➞ -33
# -11 + -22 = -33

Notes

There is at least one negative integer."""
"""import re
def negative_sum(chars):    
    chars = re.sub('%|&'," ", chars)
    chars = re.sub('-', " -", chars)
    return sum(i for i in list(map(int,chars.split())) if i < 0)

print(negative_sum("-12 13%14&-11"))
print(negative_sum("22 13%14&-11-22 13 12"))"""

import re
def negative_sum(chars):
    return sum(map(int,re.findall(r'-\d+', chars)))

print(negative_sum("-12 13%14&-11"))
print(negative_sum("22 13%14&-11-22 13 12"))

"""import re
negative_sum=lambda s:sum(map(int,re.findall('-\d+',s)))"""
