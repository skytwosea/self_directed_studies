
def count_matches(n, m):
    nset = set()
    mset = set()

    while n > 0:
        nset.add(n % 10)
        n //= 10
    while m > 0:
        mset.add(m % 10)
        m //= 10

    ctr = 0
    for element in nset:
        if element in mset:
            ctr += 1
    return ctr

assert(count_matches(10, 30) == 1)
assert(count_matches(12345, 23456) == 4)
assert(count_matches(121212, 123123) == 2)
assert(count_matches(111, 11) == 1)
assert(count_matches(101, 10) == 2)


def pos_matches(n, m):
    ctr = 0
    while n > 0 and m > 0:
        if n % 10 == m % 10:
            ctr += 1
        n //= 10
        m //= 10
    print(f"{n}, {m}: ctr = {ctr}")
    return ctr

assert(pos_matches(10, 30) == 1)
assert(pos_matches(12345, 23456) == 0)
assert(pos_matches(121212, 123123) == 2)
assert(pos_matches(111, 11) == 2)
assert(pos_matches(101, 10) == 0)
