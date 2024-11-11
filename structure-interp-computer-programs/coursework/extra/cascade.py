






def cascade(n, rcall=0):
    if n < 10:
        print(n)
    else:
        print(f"{n:<6}top ({rcall})")
        cascade(n // 10, rcall+1)
        print(f"{n:<6}bottom ({rcall})")

cascade(2023)
