# -------------------- utilities --------------------
def tree(label, branches=[]):
	for branch in branches:
		assert is_tree(branch), "branches must be trees"
	return [label] + list(branches)


def label(t):
	return t[0]


def set_label(t, v):
	t[0] = v
	return


def branches(t):
	return t[1:]


def is_tree(t):
	if type(t) != list or len(t) < 1:
		return False
	for branch in branches(t):
		if not is_tree(branch):
			return False
	return True


def is_leaf(t):
	return not branches(t)


def print_tree(t, indent=0):
	print('  ' * indent + str(label(t)))
	for b in branches(t):
		print_tree(b, indent + 1)


# ------------------ end utilities -------------------


# 1.1 Write a function that returns the height of a tree. Recall that
# the height of a tree is the length of the longest path from the root
# to a leaf.
def height(t):
	# returns integer
	if is_leaf(t):
		return 0
	maxdepth = 0
	for branch in branches(t):
		maxdepth = max(maxdepth, height(branch))
	return maxdepth + 1


assert (height(tree(3, [tree(5, [tree(1)]), tree(2)])) == 2)


# 1.2: write a function that takes in a tree and squares every value.
# It should return a new tree. Assume every item is a number.
def square_tree(t):
	if is_leaf(t):
		return tree(label(t)**2)
	return tree(label(t)**2, [square_tree(branch) for branch in branches(t)])


numbers = tree(
 1, [tree(2, [tree(3), tree(4)]),
     tree(5, [tree(6, [tree(7)]), tree(8)])])
st = square_tree(numbers)
# print("numbers:")
# print_tree(numbers)
# print("\nsquared tree:")
# print_tree(st)

# 1.3 Write a function that takes in a tree and a value x and returns a list
# containing the nodes along the path required to get from the root of the tree
# to a node containing x. If x is not present in the tree, return None. Assume
# all nodes have unique values.


def find_path(t, x):
	if label(t) == x:
		return [label(t)]
	for branch in branches(t):
		path = find_path(branch, x)
		if path:
			return [label(t)] + path


thistree = tree(2,
                [tree(7, [tree(3), tree(6, [tree(5), tree(11)])]),
                 tree(15)])
# print(find_path(thistree, 5))
assert find_path(thistree, 5) == [2, 7, 6, 5], "borked."

t = tree(1, [tree(2), tree(3)])
assert label(t) == 1
assert t[0] == 1
assert label(branches(t)[0]) == 2
assert label(branches(t)) == [2]
assert is_leaf(t[1:][1]) == True
assert [label(b) for b in branches(t)] == [2, 3]
assert branches(tree(2, tree(t, [])))[0] == [1, [2], [3]]

lst1 = [1, 2, 3]
lst2 = lst1
assert (lst1 is lst2) == True
lst2.extend([5, 6])
assert lst1[4] == 6
lst1.append([-1, 0, 1])
assert (-1 in lst1) == False
assert lst2[5] == [-1, 0, 1]
lst3 = lst2[:]
lst3.insert(3, lst2.pop(3))
assert len(lst1) == 5
assert (lst1[4] is lst3[6]) == True
assert lst3[lst2[4][1]] == 1
assert (lst1[:3] is lst2[:3]) == False
assert (lst1[:3] == lst2[:3]) == True
x = [1, 2, [4, 5, 6]]
x[2] = [3, 5, 6]
assert x == [1, 2, [3, 5, 6]]
x[2][0] = 3
assert x == [1, 2, [3, 5, 6]]

# 2.2 Write a function that takes in a value X, a value EL, and a list,
# and adds as many ELs to the end of the list as there are Xs. Make sure to
# modify the original list using list mutation techniques.


def add_this_many(x, el, lst):
	"""
	Adds el to the end of lst the number of times x occurs
	in lst.
	>>> lst = [1, 2, 4, 2, 1]
	>>> add_this_many(1, 5, lst)
	>>> lst
	[1, 2, 4, 2, 1, 5, 5]
	>>> add_this_many(2, 2, lst)
	>>> lst
	[1, 2, 4, 2, 1, 5, 5, 2, 2]
	"""
	lst.extend([el for i in range(x)])


# 2.3 Write a function that takes in a sequence s and a function fn, and returns
# a dictionary.
# The values of the dictionary are lists of elements from s. Each element e in a list
# should be constructed such that fn(e) is the same for all elements in that list.
# The key for each value should be fn(e).


def group_by(s, fn):
	"""
	>>> group_by([12, 23, 14, 45], lambda p: p // 10)
	{1: [12, 14], 2: [23], 4: [45]}
	>>> group_by(range(-3, 4), lambda x: x * x)
	{0: [0], 1: [-1, 1], 4: [-2, 2], 9: [-3, 3]}
	"""
	host = {}
	for i in s:
		c = fn(i)
		if c in host.keys():
			host[c].append(i)
		else:
			host[c] = [i]
	return host


assert group_by([12, 23, 14, 45], lambda p: p // 10) == {
 1: [12, 14],
 2: [23],
 4: [45]
}
assert group_by(range(-3, 4), lambda x: x * x) == {
 0: [0],
 1: [-1, 1],
 4: [-2, 2],
 9: [-3, 3]
}

# 2.4: implement PARTITION_OPTIONS which outputs all the ways to partition a number TOTAL using
# numbers no larger than BIGGEST.


def partition_options(total, biggest):
	if total == 0:
		return 1
	elif total < 0:
		return 0
	elif biggest == 0:
		return 0
	else:
		with_biggest = partition_options(total - biggest, biggest)
		without_biggest = partition_options(total, biggest - 1)
		print(f"wb: {with_biggest}, wob: {without_biggest}")
		return with_biggest + without_biggest


# assert partition_options(2, 2) == [[2], [1, 1]]
