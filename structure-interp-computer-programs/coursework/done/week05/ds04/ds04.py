# 1.1: You want to go up a flight of stairs that has n steps. You can either take 1
# or 2 steps each time. How many different ways can you go up this flight of
# stairs? Write a function count_stair_ways that solves this problem. Assume
# n is positive.

def stairs(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    return sum([stairs(n-1), stairs(n-2)])




# Consider a special version of the count_stairways problem, where instead
# of taking 1 or 2 steps, we are able to take up to and including k steps at
# a time.
# Write a function count_k that figures out the number of paths for this sce-
# nario. Assume n and k are positive.

def count_k(n, k=2):
    if n < 0:
        return 0
    if n == 0:
        return 1
    else:
        result = 0
        for m in range(1,k+1):
            result += count_k(n-m,k)
        return result


# x = count_k(3,3)
# print(x)
assert count_k(3,3) == 4, f"result: {count_k(3,3)}"
assert count_k(4,4) == 8, f"result: {count_k(4,4)}"
assert count_k(10,3) == 274, f"result: {count_k(10,3)}"
assert count_k(300,1) == 1, f"result: {count_k(300,1)}"
assert stairs(5) == count_k(5)
assert stairs(13) == count_k(13)




# 2.1

a = [1, 5, 4, [2, 3], 3]
assert a[0] == 1
assert a[-1] == 3
assert len(a) == 5
assert (2 in a) == False
assert (4 in a) == True
assert a[3][0] ==2






# 2.2 Write a function that takes a list s and returns a new list that keeps only
# the even-indexed elements of s and multiplies them by their corresponding
# index.

def feven(s):
    return [k*i for i,k in enumerate(s) if i % 2 == 0] # i is the enumerant, k is the list element

assert feven([1,2,3,4,5,6]) == [0,6,20]






# 2.3 Write a function that takes in a list and returns the maximum product that
# can be formed using nonconsecutive elements of the list. The input list will
# contain only numbers greater than or equal to 1.

def biggus(s):
    if len(s) == 0:
        return 1

    else:
        return max(biggus(s[1:]), s[0]*biggus(s[2:]))  # fuck me. This makes me feel stupid.

assert biggus([10,3,1,9,2]) == 90
assert biggus([5,10,5,10,5])  == 125
assert biggus([]) == 1
