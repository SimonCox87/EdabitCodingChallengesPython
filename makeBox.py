"""Create a function that creates a box based on dimension n.
Examples

make_box(5) ➞ [
  "#####",
  "#   #",
  "#   #",
  "#   #",
  "#####"
]

make_box(3) ➞ [
  "###",
  "# #",
  "###"
]

make_box(2) ➞ [
  "##",
  "##"
]

make_box(1) ➞ [
  "#"
]"""

def make_box(n):
    return["#" * n if i==0 or i==n - 1 else "#" + " " * (n - 2) + "#" for i in range(n)]

print(make_box(5))
print(make_box(3))
print(make_box(2))
print(make_box(1))
        
        