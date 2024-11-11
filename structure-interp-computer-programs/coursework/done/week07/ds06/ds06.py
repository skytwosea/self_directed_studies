# 1.2 Write a function that takes in a number n and returns a one-argument function.
# The returned function takes in a function that is used to update n. It should return
# the updated n.


def memory(n):
    """
    >>> f = memory(10)
    >>> f(lambda x: x * 2)
    20
    >>> f(lambda x: x - 7)
    13
    >>> f(lambda x: x > 5)
    True
    """

    def editor(fn):
        nonlocal n
        n = fn(n)
        return n

    return editor


# 1.3 Write a function that takes in no arguments and returns two functions, PREPEND and GET,
# which represent the 'add to front of list' and 'get the ith item' operations, respectively.
# Do not use any python built-in data structures like lists or dictionaries.


def nonlocalist():
    """
    >>> prepend, get = nonlocalist()
    >>> prepend(2)
    >>> prepend(3)
    >>> prepend(4)
    >>> get(0)
    4
    >>> get(1)
    3
    >>> get(2)
    2
    >>> prepend(8)
    >>> get(2)
    3
    """
    get = lambda x: "Index out of range!"
    k = 0

    def prepend(value):
        nonlocal get
        f = get

        def get(i):
            if i == 0:
                return value
            return f(i - 1)

    return prepend, lambda x: get(x)


# 2.1 Write a generator function MERGE that takes in two infinite generators A and B that
# are in increasing order without duplicates, and returns a generator that has all the
# elements of both generators, in increasing order, without duplicates.


def sequence(start, step):
    while True:
        yield start
        start += step


def merge(a, b):
    """
    >>> def sequence(start, step):
    ...     while True:
    ...         yield start
    ...         start += step
    >>> a = sequence(2, 3) # 2, 5, 8, 11, 14, ...
    >>> b = sequence(3, 2) # 3, 5, 7, 9, 11, 13, 15, ...
    >>> result = merge(a, b) # 2, 3, 5, 7, 8, 9, 11, 13, 14, 15
    >>> [next(result) for _ in range(10)]
    [2, 3, 5, 7, 8, 9, 11, 13, 14, 15]
    """
    x, y = next(a), next(b)
    while True:
        if x == y:
            yield x
            x, y = next(a), next(b)
        if x < y:
            yield x
            x = next(a)
        if x > y:
            yield y
            y = next(b)


# 2.2 Write a generator function GENERATE_SUBSETS that returns all subsets of the positive
# integers from 1 to n. Each call to this generator's NEXT method will return a list of
# subsets of the set [1, 2, ..., n], where n is the number of previous calls to next().


def generate_subsets():
    """
    >>> subsets = generate_subsets()
    >>> for _ in range(3):
    ...     print(next(subsets))
    ...
    [[]]
    [[], [1]]
    [[], [1], [2], [1, 2]]
    """
    starter = [[]]
    idx = 1
    while True:
        yield starter
        starter += [s + [idx] for s in starter]
        idx += 1


# tree support


def tree(label, branches=[]):
    for branch in branches:
        assert is_tree(branch), "branches must be trees"
    return [label] + list(branches)


def label(tree):
    return tree[0]


def branches(tree):
    return tree[1:]


def is_tree(tree):
    if type(tree) != list or len(tree) < 1:
        return False
    for branch in branches(tree):
        if not is_tree(branch):
            return False
    return True


def is_leaf(tree):
    return not branches(tree)


# 2.3 Implement sum_paths_gen, which takes in a tree t and returns a generator which
# yields the sum of all the nodes from a path from the root of a tree to a leaf.
# You may yield the sums in any order.


def sum_paths_gen(t):
    """
    >>> t1 = tree(5)
    >>> next(sum_paths_gen(t1))
    5
    >>> t2 = tree(1, [tree(2, [tree(3), tree(4)]), tree(9)])
    >>> sorted(sum_paths_gen(t2))
    [6, 7, 10]
    """
    pass
    if is_leaf(t):
        yield label(t)
    for branch in branches(t):
        for k in sum_paths_gen(branch):
            yield k + label(t)


# Trie recursion


def print_tree(t, indent=0):
    """Print a representation of this tree in which each node is
    indented by two spaces times its depth from the root.

    >>> print_tree(tree(1))
    1
    >>> print_tree(tree(1, [tree(2)]))
    1
      2
    >>> numbers = tree(1, [tree(2), tree(3, [tree(4), tree(5)]), tree(6, [tree(7)])])
    >>> print_tree(numbers)
    1
      2
      3
        4
        5
      6
        7
    """
    print('  ' * indent + str(label(t)))
    for b in branches(t):
        print_tree(b, indent + 1)


def collect_words(t):
    """Return a list of all the words contained in the tree where the value of each node in
    the tree is an individual letter. Words terminate at the leaf of a tree.
    >>> greetings = tree('h', [tree('i'),
    ... tree('e', [tree('l', [tree('l', [tree('o')])]),
    ... tree('y')])])
    >>> print_tree(greetings)
    h
      i
      e
        l
          l
            o
        y
    >>> collect_words(greetings)
    ['hi', 'hello', 'hey']
    """
    if is_leaf(t):
        return [label(t)]
    words = []
    for branch in branches(t):
        words += [label(t) + word for word in collect_words(branch)]
    return words
