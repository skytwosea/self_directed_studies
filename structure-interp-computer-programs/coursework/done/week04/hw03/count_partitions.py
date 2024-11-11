def ctpt(n, m):
    if n == 0:
        return 1
    elif n < 0:
        return 0
    elif m == 0:
        return 0
    else:
        with_m = ctpt(n-m, m)
        without_m = ctpt(n, m-1)
        return with_m + without_m