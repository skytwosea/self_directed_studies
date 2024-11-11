
# 1.2: rewrite the following as a lambda function:
def curry2(h):
    def f(x):
        def g(y):
            return h(x, y)
        return g
    return f
make_adder = curry2(lambda x, y: x + y)
add_three = make_adder(3)
add_four = make_adder(4)
five = add_three(2)

curry3 = lambda h: lambda x: lambda y: h(x, y)
mkadd = curry3(lambda x, y: x+y)
adthre = mkadd(3)
adfor = mkadd(4)
faival = adthre(2)

assert five == faival




# 1.4: rewrite the following as a lambda function:
y = "y"
h = y
def y(y):
    h = "h"
    if y == h:
        return y + "i"
    y = lambda y: y(h) # h has been set to "h" so this
                       # function can recurse only once
    return lambda h: y(h)
y = y(y)(y)
# print(f"y: {y}")

z = lambda y: y+"i" if y=="h" else lambda h: "h"+"i"
z = z(y)(y)
# print(f"z: {z}")

assert y == z





# 1.5: Write a function that takes in a function COND
# and a number N and prints numbers from 1 to N
# where calling COND on that number returns TRUE
# aka:
# print all integers 1..i where COND is TRUE

def ints(cond, n):
    result = []
    for i in range(1, n+1):
        result.append(i) if cond(i) else None
    return result

evens = lambda x: True if x%2==0 else False
odds  = lambda y: True if y%2!=0 else False

assert(ints(odds, 5) == [1,3,5])
assert(ints(evens, 5) == [2,4])





# 1.6: Write a function similar to keep_ints like before, but now it takes in a
# number n and returns a function that has one parameter cond. The returned
# function prints out numbers from 1 to n where calling cond on that number
# returns True.

def keeper(n):
    def f(cond):
        result = []
        for i in range(1, n+1):
            result.append(i) if cond(i) else None
        return result
    return f

evens = lambda x: True if x%2==0 else False
odds  = lambda y: True if y%2!=0 else False

fn = keeper(5)
assert(fn(odds) == [1,3,5])
assert(fn(evens) == [2,4])




# 1.1: Write a function print delayed delays printing its argument until the next
# function call. print delayed takes in an argument x and returns a new func-
# tion delay print. When delay print is called, it prints out x and returns
# another delay print.
pdlst = [] # holds values that would otherwise be printed, for testing
def print_delayed(x):
    def delay_print(y):
        # print(x)
        pdlst.append(x)
        return print_delayed(y)
    return delay_print

f = print_delayed(1)
f = f(2)
f = f(3)
f = f(4)(5)
f = f("hi")

assert(pdlst == [1,2,3,4,5])
assert(callable(f) == True)




# 1.2: Write a function print_n that can take in an integer n and returns a
# repeatable print function that can print the next n parameters. After
# the nth prameter, it just prints 'done'.
rplst = []
def print_n(n):
    def rprint(rpt):
        if n <= 0:
            rplst.append("done")
        else:
            rplst.append(rpt)
        m = n - 1
        return print_n(m)
    return rprint

f = print_n(2)
f = f("hi")
f = f("hello")
f = f("bye")
g = print_n(1)
h = g("first")("second")("third")

assert(rplst == ["hi", "hello", "done", "first", "done", "done"])
assert(callable(h) == True)




print("all tests passed!")
