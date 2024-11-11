
# 2.3: Define a function, count digits, which takes in an integer, n, and counts the number
# of digits in that number.
def dcount(x):
    ctr = 0
    while x > 0:
        ctr += 1
        x //= 10
    return ctr

assert(dcount(12345678) == 8)
assert(dcount(3652) == 4)
assert(dcount(0) == 0)




# 2.4: Define a function, count matches, which takes in two integers n and m, and counts
# the number of digits that match.
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
    # print(f"{n}, {m}: ctr = {ctr}")
    return ctr

assert(pos_matches(10, 30) == 1)
assert(pos_matches(12345, 23456) == 0)
assert(pos_matches(121212, 123123) == 2)
assert(pos_matches(111, 11) == 2)
assert(pos_matches(101, 10) == 0)




# 4.3: Define a function, count matches, which takes in two integers n and m, and counts
# the number of digits that match.
lpow = lambda x, y: x**y

def dpow(x, y):
    return x ** y

assert(lpow(6,7) == dpow(6,7))
assert(lpow(2,-3) == dpow(2,-3))




# 4.5: Write make skipper, which takes in a number n and outputs a function. When
# this function takes in a number x, it prints out all the numbers between 0 and x,
# skipping every nth number (meaning skip any value that is a multiple of n).
def skip(n):
    def do_skip(m):
        result = []
        for i in range(m+1):
            if i%n != 0:
                result.append(i)
        return result
    return do_skip

fn = skip(2)
assert(fn(5) == [1,3,5])


# 5.1: Define a function, ordered digits, which takes in a positive integer, x, and returns
# True if the (base 10) digits of x are in non-decreasing order, and False otherwise.

def ordered(x):
    rev = []
    while x > 0:
        rev.insert(0, x % 10)
        x //= 10
    for i in range(1,len(rev)):
        if rev[i-1] > rev[i]:
            return False
    return True

assert(ordered(5) == True)
assert(ordered(11) == True)
assert(ordered(127) == True)
assert(ordered(1357) == True)
assert(ordered(21) == False)
result = ordered(1375)
assert(result == False)




# 5.3: Define a function, cycle, which takes in three functions, f1, f2, f3, and returns a
# function that takes in an integer n and returns a function that takes in an integer
# x, and returns the result of f1(x) the first time it’s called, f2(x) the second time it’s
# called, f3(x) the third time it’s called, and then cycles back to f1(x) the fourth time
# it’s called, and so on.

# identity = lambda x: x
add1     = lambda x: x + 1
times2   = lambda x: x * 2
add3     = lambda x: x + 3

def cycle(f1, f2, f3):
    fnlst = [f1, f2, f3]
    compose  = lambda f, g: lambda x: f(g(x))
    def do_cycle(n):
        fn = lambda x: x
        if n != 0:
            for i in range(n):
                fn = compose(fnlst[i%3], fn)
        return fn
    return do_cycle

my_cycle = cycle(add1, times2, add3)

identity = my_cycle(0)
# print(f"identity(f) == 5 : {identity(5)}")
assert(identity(5) == 5)

add_one_then_double = my_cycle(2)
# print(f"add_one_then_double(1) == 4 : {add_one_then_double(1)}")
assert(add_one_then_double(1) == 4)

do_all_functions = my_cycle(3)
# print(f"do_all_functions(2) == 9 : {do_all_functions(2)}")
assert(do_all_functions(2) == 9)

do_more_than_a_cycle = my_cycle(4)
# print(f"do_more_than_a_cycle(2) == 10 : {do_more_than_a_cycle(2)}")
assert(do_more_than_a_cycle(2) == 10)

do_two_cycles = my_cycle(6)
# print(f"do_two_cycles(1) == 19 : {do_two_cycles(1)}")
assert(do_two_cycles(1) == 19)






# 5.3: Define a function, is palindrome, which takes in an integer, n, and returns True if
# n is a palindrome and False otherwise.
def pal(n):
    m, rev = n, 0
    while m > 0:
        rev *= 10
        rev += (m % 10)
        m //= 10
    return n == rev

assert(pal(12321) == True)
assert(pal(42) == False)
assert(pal(2015) == False)
assert(pal(55) == True)




print("all tests passed!")