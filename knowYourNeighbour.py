# Create a function that takes a string as an argument and returns True if each letter in the string is surrounded by a plus sign. 
# Return False otherwise.

# Examples

# plus_sign("+f+d+c+#+f+") ➞ True

# plus_sign("+d+=3=+s+") ➞ True

# plus_sign("f++d+g+8+") ➞ False

# plus_sign("+s+7+fg+r+8+") ➞ False

# Notes

# For clarity, each letter must have a plus sign on both sides.

import re
def plus_sign(txt):
    return re.findall('(?<=\+)[a-z](?=\+)',txt) == [i for i in txt if i.isalpha()]
	

print(plus_sign("+f+d+c+#+f+")) # ➞ True
print(plus_sign("+d+=3=+s+")) # ➞ True
print(plus_sign("f++d+g+8+")) # ➞ False
print(plus_sign("+s+7+fg+r+8+")) # ➞ False

def plus_sign(txt):
	return all(x in txt for x in ['+' + i + '+' for i in txt if i.isalpha()])