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
    def pp(k, lim, value, chooser):
        if k >= lim:
            return value
        if k % 7 == 0 or num_sevens(k) > 0:
            return pp(k+1,
                      lim,
                      ((lambda x: x-1) if chooser == "up" else (lambda x: x+1))(value),
                      ("down" if chooser == "up" else "up"))
        return pp(k+1,
                  lim,
                  ((lambda x: x+1) if chooser == "up" else (lambda x: x-1))(value),
                  chooser)

    return pp(1, n, 1, "up")

# print(pingpong(9))
