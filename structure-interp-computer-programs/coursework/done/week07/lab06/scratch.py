def countdown(n):
    print("Beginning countdown!")
    while n >= 0:
        yield n
        n -= 1
    print("blastoff!")


# def make_fib():
#     memo = []
#     def fib():
#         if not memo:
#             memo.append(0)
#             yield memo[0]
#         if len(memo) == 1:
#             memo.append(1)
#             yield memo[1]
#         while len(memo) >= 2:
#             memo.append(memo[-1] + memo[-2])
#             yield memo[-1]
#     return fib


def make_fib():
    memo = []
    def fib():
        nonlocal memo
        if not memo:
            memo.append(0)
            return memo[0]
        if len(memo) == 1:
            memo.append(1)
            return memo[1]
        if len(memo) >= 2:
            memo.append(memo[-1] + memo[-2])
            return memo[-1]
    return fib

