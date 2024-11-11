# 1.1 Write a function that takes in the current temperature and a boolean value telling
# if it is raining and returns True if Alfonso will wear a jacket and False otherwise.

def jackit(t, r):
    return True if (t < 60 or r) else False

assert(jackit(90, False) == False)
assert(jackit(40, False) == True)
assert(jackit(100, True) == True)





# 1.3: is it prime? for the zillionth time?

def prime(n):
    m = 2
    while m < n**(1/2):
        if n % m == 0:
            return False
        m +=  1
    return True

assert(prime(10) == False)
assert(prime(7) == True)




# rest are drawings








print("all tests passed!")
