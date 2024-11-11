lst = [1,2,3,4,5]
assert lst[1:3] == [2,3]
assert lst[-4] == 2




# 1.3: Implement a function map mut that takes a list as an argument and maps a function
# f onto each element of the list. You should mutate the original lists, without creating
# any new lists. Do NOT return anything.

def mmut(f, s):
    # for i in range(len(s)):
    #     s[i] = f(s[i]) # alters s in place

    # return [f(i) for i in s] # creates a different list

    for i, k in enumerate(s): s[i] = f(k) # alters s in place


s = [1,2,3,4]
mmut(lambda x: x**2, s)
assert s == [1,4,9,16], f"s: {s}, mmut:{mmut(lambda x: x**2, s)}"




# 1.10: Consider an insect in an M by N grid. The insect starts at the bottom left corner,
# (0, 0), and wants to end up at the top right corner (M-1, N-1). The insect is only
# capable of moving right or up. Write a function paths that takes a grid length and
# width and returns the number of different paths the insect can take from the start
# to the goal. (There is a closed-form solution to this problem, but try to answer it
# procedurally using recursion.)

def paths(m,n):
    if m <= 0 or n <= 0:
        return 0
    if m == 1 or n == 1:
        return 1
    return paths(m-1,n) + paths(m, n-1)

assert paths(2,2) == 2
assert paths(117,1) == 1





# 1.11: Write a procedure merge(s1, s2) which takes two sorted (smallest value first) lists
# and returns a single list with all of the elements of the two lists, in ascending order.
# Use recursion.
# Hint: If you can figure out which list has the smallest element out of both, then we
# know that the resulting merged list will have that smallest element, followed by the
# merge of the two lists with the smallest item removed. Don’t forget to handle the
# case where one list is empty!

def merge(s1, s2):
    if len(s1) == 0:
        return s2
    if len(s2) == 0:
        return s1

    return [ min(s1[0], s2[0]), max(s1[0], s2[0]) ] + merge(s1[1:], s2[1:])

assert merge([1,3], [2,4]) == [1,2,3,4], f"{merge([1,3], [2,4])}"
assert merge([1,2], []) == [1,2], f"{merge([1,2], [])}"





# 1.12: Mario needs to jump over a sequence of Piranha plants, represented as a string of
# dashes (no plant) and P’s (plant!). He only moves forward, and he can either step
# (move forward one place) or jump (move forward two places) from each position.
# How many different ways can Mario traverse a level without stepping or jumping
# into a Piranha plant? Assume that every level begins with a dash (where Mario
# starts) and ends with a dash (where Mario must end up):
# Hint: You can get the ith character in a string s by using s[i]. For example,
# >>> s = 'abcdefg'
# >>> s[0]
# 'a'
# >>> s[2]
# 'c'
# You can find the total number of characters in a string with the built-in len function:
# >>> s = 'abcdefg'
# >>> len(s)
# 7
# >>> len('')
# 0

def mario_number(level):

    if len(level) - 1 == 0:
        return 1
    if len(level) <= 0 or level[0] == 'P':
        return 0
    return mario_number(level[1:]) + mario_number(level[2:])

assert mario_number('-P-P-') == 1, f"{mario_number('-P-P-')}"
assert mario_number('-P-P--') == 1, f"{mario_number('-P-P--')}"
assert mario_number('--P-P-') == 1, f"{mario_number('--P-P-')}"
assert mario_number('---P-P-') == 2, f"{mario_number('---P-P-')}"
assert mario_number('-P-PP-') == 0, f"{mario_number('-P-PP-')}"
assert mario_number('----') == 3, f"{mario_number('----')}"
assert mario_number('----P----') == 9, f"{mario_number('----P----')}"
assert mario_number('---P----P-P---P--P-P----P-----P-') == 180, f"{mario_number('---P----P-P---P--P-P----P-----P-')}"
