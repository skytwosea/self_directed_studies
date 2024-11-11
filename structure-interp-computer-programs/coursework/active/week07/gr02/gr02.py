from random import randint

# a = 1
# b = 2
# dt = {a: 1, b: 2}

# a = [1]
# b = [2]
# dt = {a: 1, b: 2} # unhashable type: list

a = [1, [2, 3], 4]
c = a[1]
assert c == [2, 3]

a.append(c)
assert a == [1, [2, 3], 4, [2, 3]]
c[0] = 0
assert c == [0, 3]
assert a == [1, [0, 3], 4, [0, 3]]
a.extend(c)
c[1] = 9
assert a == [1, [0, 9], 4, [0, 9], 0, 3]

list1 = [1, 2, 3]
list2 = [1, 2, 3]
assert list1 == list2
assert list1 is not list2

# append: add an item to the end of a list, whatever its type; e.g. if it's
# a list, then the last item will be that list
# extend: add the items of one list to the end of another list. This operation
# changes the first list.
# + operator for lists: similar result to extend but creates a new object.
assert list1 + list2 == [1, 2, 3, 1, 2, 3]
list1.extend(list2)

a = [1, 2, [3, 4], 5]
b = a[:]
b[1] = 6
b[2][0] = 7
assert b == [1, 6, [7, 4], 5]
assert b != a

# apparently, the two types of functions necessary to make an abstract data type
# are CONSTRUCTORS and SELECTORS. Constructors _build_ the ADT, and selectors
# retrieve data from an instantiated ADT.


def rational(num, den):
    return [num, den]


def numer(x):
    return x[0]


def denom(x):
    return x[1]


def gcd(a, b):
    x = max(a, b)
    y = min(a, b)
    r = x % y
    if r == 0:
        return y
    return gcd(y, r)


def simplify(f1):
    g = gcd(f1[0], f1[1])
    return rational(numer(f1) // g, denom(f1) // g)


def multiply(f1, f2):
    r = rational(numer(f1) * numer(f2), denom(f1) * denom(f2))
    return simplify(r)


x = rational(1, 2)
y = rational(2, 3)
# print(multiply(x, y))

# violating/breaking an abstraction barrier means using a lower level function when
# one could be using a higher level function. For example, simplify() uses numer()
# denom(). If simplify were to reach into the list directly using indexing, we'd be
# breaking the abstraction barrier.
# In general, abstraction barriers make programs easier to maintain and modify.

# you know what? Fuck your list based trees. I'm doing this with classes.


class Tree():

    def __init__(self, label=None, left=None, right=None):
        self.label = label
        self.left = left
        self.right = right

    def label(self):
        return self.label

    def is_leaf(self):
        return self.left is None and self.right is None

    def add(self, val):
        if not self.label and self.is_leaf():
            self.label = val
            return
        if val <= self.label:
            if not self.left:
                self.left = Tree(label=val)
            else:
                Tree.add(self.left, val)
        else:
            if not self.right:
                self.right = Tree(label=val)
            else:
                Tree.add(self.right, val)

    def is_min_heap(tree):
        if tree.is_leaf():
            return True
        if tree.left and tree.label > tree.left.label or tree.right and tree.label > tree.right.label:
            return False
        return tree.is_min_heap(tree.left) and tree.is_min_heap(tree.right)

    def tp(self, indent=0):
        print(" " * indent + str(self.label).ljust(3))
        if self.right is not None:
            Tree.tp(self.right, indent=indent + 2)
        if self.left is not None:
            Tree.tp(self.left, indent=indent + 2)
        return


test_array = [randint(1, 100) for i in range(10)]
t = Tree()
for i in test_array:
    t.add(i)

# ok fine...


def tree(label, branches=[]):
    for b in branches:
        assert is_tree(b), 'branches must be trees'
    return [label] + list(branches)


def is_tree(tree):
    if type(tree) != list or len(tree) < 1:
        return False
    for b in branches(tree):
        if not is_tree(b):
            return False
    return True


def label(tree):
    return tree[0]


def branches(tree):
    return tree[1:]


def is_leaf(tree):
    return not tree[1:]


def is_min_heap(tree):
    if is_leaf(tree):
        return True
    if not all([label(tree) <= label(b) for b in branches(tree)]):
        return False
    return all([is_min_heap(b) for b in branches])


def largest_product_path(tree):
    if is_leaf(tree):
        return label(tree)
    return label(tree) * max([largest_product_path(b) for b in branches(tree)])


def max_tree(t):
    if label(t) >= all([label(m) for m in branches(t)]):
        return max_tree(branches(t))
    else:
        new_branches = tree(label(t), branches(t))
        new_label = max(label(m) for m in branches(t))
        return max_tree(tree(new_label, new_branches))


def make_max_finder():
    max_tracker = 0

    def mf(newlist):
        nonlocal max_tracker
        candidate = max(newlist)
        if candidate > max_tracker:
            max_tracker = candidate
        return max_tracker

    return mf


f = make_max_finder()
assert f([5, 6, 7]) == 7
assert f([1, 2, 3]) == 7
assert f([9]) == 9
fn = make_max_finder()
assert fn([1]) == 1

# Iterable: object which can be looped over using a for loop
#    lists, tuples, sets, dicts, strings, more
# Any value that can produce iterators is called an iterable value. Anything
# that can be passed into the built-in iter function.

# Iterator: object that allows you to iterate over iterables
# Iterators provide sequential access to values, one by one

# Generator: a function that allows you to declare a function
# that behaves like an iterator
# An iterator returned by a special class of function called a generator function
# distinguished from regular functions by their use of yield statements


def black_hole(seq, trap):
    seq = iter(seq)
    candidate = next(seq)
    while candidate != trap:
        yield candidate
        candidate = next(seq)
    while True:
        yield trap


# use a for loop
