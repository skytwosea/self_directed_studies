# RECURSION

# 1.1 Write a function that takes two numbers m and n and returns their product
# assume m and n are positive ints. Use recursion, not mul or *

def mulf(m, n):

    if n <= 0:
        return 0
    return m + mulf(m, n-1)

assert(mulf(5,3) == 15)
assert(mulf(6, 8) == 48)
assert(mulf(1,19) == 19)
assert(mulf(0,32) == 0)



# 1.2 recursive power: 

def powf(x,y):
    if y > 0:
        return x * powf(x, y-1)
    return 1

assert(powf(5,4) == 625)




# 1.3 hailstone: pick a positive integer n to start. If n is even, divide by 2. If n is odd,
# multiply by 3 and add 1. Repeat until n == 1. 

haillst = []
def hail(n):
    if n == 1:
        haillst.append(n)
        return len(haillst)
    haillst.append(n)
    if n % 2 == 0:
        return hail(n//2)
    return hail(n*3+1)

h = hail(10)
assert (haillst == [10,5,16,8,4,2,1])
assert(h == 7)




# 1.4: implement a recursive is_prime function. 
from math import sqrt

def prime(n, k=2):
    if n == 1 or n % k == 0:
        return False
    if k < sqrt(n):
        return prime(n, k+1)
    return True


assert(prime(1) == False)
assert(prime(3) == True)
assert(prime(8) == False)
assert(prime(17) == True)
assert(prime(54) == False)
assert(prime(107) == True)




# 1.5: write a procedure which takes two numbers and returns a single
# number with all of their digits organized in decreasing order.
# treat zero as having no digits.
#
# >>> merge(31, 42)
# 4321
# >>> merge(21, 0)
# 21
# >>> merge (21, 31)
# 3211

def merge(n, m, first=True):
    if first:
        n, m = list(str(n)), list(str(m))

    if len(m) <= 0:
        return int(''.join(n))
    
    toinsert = m.pop()
    k = 0
    for i in range(len(n)):
        if toinsert < n[i]:
            k += 1
        else:
            n.insert(k, toinsert)
            break

    return merge(n, m, False)



assert(merge(31, 42) == 4321)
assert(merge(21, 0) == 21)
assert(merge(21, 31) == 3211)





# 1.6 Define a function make fn repeater which takes in a one-argument function
# f and an integer x. It should return another function which takes in one
# argument, another integer. This function returns the result of applying f to
# x this number of times.
#
# >>> incr_1 = make_func_repeater(lambda x: x + 1, 1)
# >>> incr_1(2) #same as f(f(x))
# 3
# >>> incr_1(5)
# 6

# composer = lambda f: lambda x: f(f(x))

def fnrpt(f, x):
    def repeater(k):
        if k > 1: # the last application of f is in the else: block
            return f(repeater(k-1))
        else:
            return f(x)
    return repeater

incr_1 = fnrpt(lambda x: x+1, 1)
assert(incr_1(2) == 3)
assert(incr_1(5) == 6)





print("all tests passed!")
