def generator_1():
    pass


def factorial_throw_generator():
    pass



def factorials_up_to(x):
    a = 1
    if x ==0:
        yield 1
    for i in range(1, x+1):
        a *= i
        yield a,"atul"


#how to add 0!    ????
counter =0
for x in factorials_up_to(6):
    counter += 1
    print(counter, x)
    
#why not correct ???    
for x in range(6):
    print(factorials_up_to(x))

    
    
    
import itertools


def factorial_generator():
    i, fac = 1, 1
    while True:
        yield fac
        fac *= i
        i += 1

def factorial(n):
    return next(itertools.islice(factorial_generator(), n, None))

for i in range(11):
    print(factorial(i))    
    
    
    
    
def fact(x):
    a = 1
    b = 1
    if x == 0:
        a = 1
    if x < 0:
        print('enter valid whole number!')
    if x > 0:
        while b < x:
            a = a * b
            b += 1
    return a
#main
z = 31
g = (fact(n) for n in range (0,int(z)))
for i in range(31):
    print(next(g))