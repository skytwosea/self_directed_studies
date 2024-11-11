HW_SOURCE_FILE = 'hw03.py'

#############
# Questions #
#############

def num_sevens(x):
    """Returns the number of times 7 appears as a digit of x.

    >>> num_sevens(3)
    0
    >>> num_sevens(7)
    1
    >>> num_sevens(7777777)
    7
    >>> num_sevens(2637)
    1
    >>> num_sevens(76370)
    2
    >>> num_sevens(12345)
    0
    >>> from construct_check import check
    >>> # ban all assignment statements
    >>> check(HW_SOURCE_FILE, 'num_sevens',
    ...       ['Assign', 'AugAssign'])
    True
    """

    if x < 7:
        return 0
    if x == 7:
        return 1
    return 1 + num_sevens(x // 10) if x % 10 == 7 else num_sevens(x // 10)





# a = lambda x: x + 1
# s = lambda x: x - 1

def pingpong(n):
    """Return the nth element of the ping-pong sequence.

    >>> pingpong(7)
    7
    >>> pingpong(8)
    6
    >>> pingpong(15)
    1
    >>> pingpong(21)
    -1
    >>> pingpong(22)
    0
    >>> pingpong(30)
    6
    >>> pingpong(68)
    2
    >>> pingpong(69)
    1
    >>> pingpong(70)
    0
    >>> pingpong(71)
    1
    >>> pingpong(72)
    0
    >>> pingpong(100)
    2
    >>> from construct_check import check
    >>> # ban assignment statements
    >>> check(HW_SOURCE_FILE, 'pingpong', ['Assign', 'AugAssign'])
    True
    """
    def pp(k, value, chooser):
        if k >= n:
            return value
        if k % 7 == 0 or num_sevens(k) > 0:
            return pp(k+1,
                      ((lambda x: x-1) if chooser == "up" else (lambda x: x+1))(value),
                      ("down" if chooser == "up" else "up"))
        return pp(k+1,
                  ((lambda x: x+1) if chooser == "up" else (lambda x: x-1))(value),
                  chooser)
    
    return pp(1, 1, "up")





from math import log

def count_change(total):
    """Return the number of ways to make change for total.

    >>> count_change(7)
    6
    >>> count_change(10)
    14
    >>> count_change(20)
    60
    >>> count_change(100)
    9828
    >>> from construct_check import check
    >>> # ban iteration
    >>> check(HW_SOURCE_FILE, 'count_change', ['While', 'For'])
    True
    """

    def partitions(n, m):
        if n == 0:
            return 1

        elif n < 0 or m == 0:
            return 0

        elif not (log(m, 2)).is_integer():
            return partitions(n, m-1)

        else:
            wm = partitions(n-m, m)
            wom = partitions(n, m-1)
            return wm + wom

    return partitions(total, total)






def missing_digits(n):
    """Given a number a that is in sorted, increasing order,
    return the number of missing digits in n. A missing digit is
    a number between the first and last digit of a that is not in n.
    >>> missing_digits(1248) # 3, 5, 6, 7
    4
    >>> missing_digits(1122) # No missing numbers
    0
    >>> missing_digits(123456) # No missing numbers
    0
    >>> missing_digits(3558) # 4, 6, 7
    3
    >>> missing_digits(4) # No missing numbers between 4 and 4
    0
    >>> from construct_check import check
    >>> # ban while or for loops
    >>> check(HW_SOURCE_FILE, 'missing_digits', ['While', 'For'])
    True
    """
    nset = {int(i) for i in list(str(n))}
    nrng = set(range(min(nset), max(nset)+1) )

    def identifier(n, missing):
        if n <= 0:
            return len(missing)
        else:
            current = n % 10
            if current in missing:
                missing.discard(current)
        return identifier(n//10, missing)

    return identifier(n, nrng)








###################
# Extra Questions #
###################

def print_move(origin, destination):
    """Print instructions to move a disk."""
    print(f"Move the top disk from rod {origin} to rod {destination}")

def move_stack(n, start, end):
    """Print the moves required to move n disks on the start pole to the end
    pole without violating the rules of Towers of Hanoi.

    n -- number of disks
    start -- a pole position, either 1, 2, or 3
    end -- a pole position, either 1, 2, or 3

    There are exactly three poles, and start and end must be different. Assume
    that the start pole has at least n disks of increasing size, and the end
    pole is either empty or has a top disk larger than the top n start disks.

    >>> move_stack(1, 1, 3)
    Move the top disk from rod 1 to rod 3
    >>> move_stack(2, 1, 3)
    Move the top disk from rod 1 to rod 2
    Move the top disk from rod 1 to rod 3
    Move the top disk from rod 2 to rod 3
    >>> move_stack(3, 1, 3)
    Move the top disk from rod 1 to rod 3
    Move the top disk from rod 1 to rod 2
    Move the top disk from rod 3 to rod 2
    Move the top disk from rod 1 to rod 3
    Move the top disk from rod 2 to rod 1
    Move the top disk from rod 2 to rod 3
    Move the top disk from rod 1 to rod 3
    """
    assert 1 <= start <= 3 and 1 <= end <= 3 and start != end, "Bad start/end"
    "*** YOUR CODE HERE ***"

    # if original stack has even number of disks, first move goes to non-target position
    # if original stack has ODD  number of disks, first move goes to TARGET     position

    # recursive steps:
        # move top N-1 disks on to the spare peg
        # move disk N to the target peg
        # move the stack N-1 onto the target peg

    """
    three disks is the base set of moves that is recursed.
    three disks: first move goes to target
    four  disks: first move goes to spare
    wherever the first of a three-disk move goes, that is where the stack of three will land
    so  if n is ODD,  first move goes to TARGET
    and if n is EVEN, first move goes to SPARE
    """

    # visualize: (incomplete)
    # poles = [[],[],[]]
    # m = 0
    # while m < n:
    #     poles[start].append(chr(m+97))
    #     m += 1

    # define which peg is auxiliary (spare)
    p = [1,2,3]
    p.remove(start)
    p.remove(end)
    spare = p[0]

    def hanoi(n, orig, dest, auxx):
        if n == 1:
            # print(f"Move the top disk from rod {orig} to rod {dest}")
            print_move(orig, dest)
            return
        hanoi(n-1, orig, auxx, dest)
        # print(f"Move the top disk from rod {orig} to rod {dest}")
        print_move(orig, dest)
        hanoi(n-1, auxx, dest, orig)

    return hanoi(n, start, end, spare)



from operator import sub, mul

def make_anonymous_factorial():
    """Return the value of an expression that computes factorial.

    >>> make_anonymous_factorial()(5)
    120
    >>> from construct_check import check
    >>> # ban any assignments or recursion
    >>> check(HW_SOURCE_FILE, 'make_anonymous_factorial', ['Assign', 'AugAssign', 'FunctionDef', 'Recursion'])
    True
    """
    # definitely didn't solve this one on my own :(
    return (lambda f: f(f))(lambda f: lambda n: 1 if n==1 else mul(n,f(f)(n-1)))