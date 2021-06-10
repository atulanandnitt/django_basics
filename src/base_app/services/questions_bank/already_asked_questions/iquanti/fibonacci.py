def fib(n):
    if n == 0 or n ==1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

for i in range(5):
    print(fib(i))


def fib_2(n):
    if n == 0 or n ==1:
        return 1
    elif n >2:
        a,b =1,1
        for _ in range(2,n):
            a, b = b, a + b
        return b

# for i in range(100):
#     print(fib(i))
fib(100)


def fib_2(n):
    if n == 0 or n ==1:
        return 1
    elif n >2:
        a,b =1,1
        for _ in range(2,n):
            a, b = b, a + b
        return b

# for i in range(100):
#     print(fib(i))
fib(100)
