"""We have two lists _N and _P, where _N represents the value of a node in Binary Tree, and _P is the parent of _N.
N	P
1	2
3	2
6	8
9	8
2	5
8	5
5	-1

Write a function to find the node type of the node within this Binary Tree, ordered by the value of the node. Output one of the following:

    Root: If node is root node.
    Leaf: If node is leaf node.
    Inner: If node is neither root nor leaf node.
    Not exist: If node not exist.

node_type([1, 3, 6, 9, 2, 8, 5], [2, 2, 8, 8, 5, 5, -1], 5) ➞ "Root"

node_type([1, 3, 6, 9, 2, 8, 5], [2, 2, 8, 8, 5, 5, -1], 6) ➞ "Leaf"

node_type([1, 3, 6, 9, 2, 8, 5], [2, 2, 8, 8, 5, 5, -1], 2) ➞ "Inner"

node_type([1, 3, 6, 9, 2, 8, 5], [2, 2, 8, 8, 5, 5, -1], 10) ➞ "Not exist"""

def node_type(_N, _P, n):
    return "Root" if n==_N[_P.index(-1)] else "Inner" if n in _P else "Leaf" if n in _N else "Not exist"

"""print(node_type([1, 3, 6, 9, 2, 8, 5], [2, 2, 8, 8, 5, 5, -1], 5)) # ➞ "Root"
print(node_type([1, 3, 6, 9, 2, 8, 5], [2, 2, 8, 8, 5, 5, -1], 6)) # ➞ "Leaf"
print(node_type([1, 3, 6, 9, 2, 8, 5], [2, 2, 8, 8, 5, 5, -1], 2)) # ➞ "Inner"
print(node_type([1, 3, 6, 9, 2, 8, 5], [2, 2, 8, 8, 5, 5, -1], 10)) # ➞ "Not exist"""

# _P shows how many children parent has.
# if n in _N and not in _P = Leaf
# if n in _P = Inner.


print(node_type([1, 3, 6, 9, 2, 8, 5], [2, 2, 8, 8, 5, 5, -1], 1 )) #, "Leaf")
print(node_type([1, 3, 6, 9, 2, 8, 5], [2, 2, 8, 8, 5, 5, -1], 2)) #, "Inner")
print(node_type([1, 3, 6, 9, 2, 8, 5], [2, 2, 8, 8, 5, 5, -1], 3)) #, "Leaf")
print(node_type([1, 3, 6, 9, 2, 8, 5], [2, 2, 8, 8, 5, 5, -1], 5)) #, "Root")
print(node_type([1, 3, 6, 9, 2, 8, 5], [2, 2, 8, 8, 5, 5, -1], 6)) #, "Leaf")
print(node_type([1, 3, 6, 9, 2, 8, 5], [2, 2, 8, 8, 5, 5, -1], 8)) #, "Inner")
print(node_type([1, 3, 6, 9, 2, 8, 5], [2, 2, 8, 8, 5, 5, -1], 9)) #, "Leaf")
print(node_type([1, 3, 6, 9, 2, 8, 5], [2, 2, 8, 8, 5, 5, -1], 10)) #, "Not exist")
print(node_type([6, 3, 1, 2, 5, 7, 4, 6, 8], [3, 1, 6, 1, 2, 3, 8, -1, 6], 8)) #, "Inner")
print(node_type([5, 6, 8, 7, 1, 9, 4, 11, 10, 2], [8, 8, -1, 8, 7, 4, 5, 4, 1, 1], 11)) #, "Leaf")
print(node_type([3, 2, 4, 9, 11, 10, 8, 5, 6, 7], [-1, 3, 3, 2, 3, 4, 4, 9, 10, 8], 3 )) #, "Root")
print(node_type([5, 6, 8, 7, 1, 9, 4, 11, 10, 2], [8, 8, -1, 8, 7, 4, 5, 4, 1, 1], 4)) #, "Inner")
print(node_type([3, 2, 4, 9, 11, 10, 8, 5, 6, 7], [-1, 3, 3, 2, 3, 4, 4, 9, 10, 8], 6)) #, "Leaf")
print(node_type([6, 3, 1, 2, 5, 7, 4, 6, 8], [3, 1, 6, 1, 2, 3, 8, -1, 6], 5)) #, "Leaf")
print(node_type([5, 6, 8, 7, 1, 9, 4, 11, 10, 2], [8, 8, -1, 8, 7, 4, 5, 4, 1, 1], 8)) #, "Root")
print(node_type([3, 2, 4, 9, 11, 10, 8, 5, 6, 7], [-1, 3, 3, 2, 3, 4, 4, 9, 10, 8], 10)) #, "Inner")"""

"""def node_type(_N, _P, n):
	if not n in _N: return "Not exist"
	if not n in _P: return "Leaf"
	if _P[_N.index(n)] == -1: return "Root"
	return "Inner"""
