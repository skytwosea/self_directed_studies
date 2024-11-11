# video 61A Spring 2020 lecture 8: Implementing Functions

# Return all digits of non-negative N that are not DIGIT,
# for some non-negative DIGIT less than 10

def remove(n, d):
    backwards = 0
    while n > 0:
        candidate = n % 10
        if candidate != d:
            backwards *= 10
            backwards += candidate
        n //= 10

    result = 0
    while backwards > 0:
        result *= 10
        result += (backwards % 10)
        backwards //= 10
    return result

assert(remove(231, 3) == 21)
assert(remove(243132, 2) == 4313)




print("all tests passed!")