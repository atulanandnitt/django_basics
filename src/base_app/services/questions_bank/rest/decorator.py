
# Decorator

def my_decorator(some_function):

    def wrapper():

        print("Something is happening before some_function() is called.")

        some_function()

        print("Something is happening after some_function() is called.")

    return wrapper


def functionNeedsDecorator():
    print("Wheee!")


functionNeedsDecorator = my_decorator(functionNeedsDecorator)

functionNeedsDecorator()




def my_decorator(some_function):

    def wrapper1():

        num = 10

        if num == 10:
            print("Yes!")
        else:
            print("No!")

        some_function()

        print("Something is happening after some_function() is called.")

    return wrapper1


# functionNeedsDecorator = my_decorator(functionNeedsDecorator)
@my_decorator
def functionNeedsDecorator():
    print("in side the real funtion")

functionNeedsDecorator()





def my_decorator(some_function1 ,a ,b):

    def wrapper1(b ,a):

        print("we want to find sum of " , a , " and ", b)

        some_function1(4 ,5)

        print("is the sum is correct for " , a , " and ", b)
    return wrapper1


def just_some_function(a1 ,b1):
    # print("Wheee!")
    print(a1 + b1)

just_some_function(44 ,55)

just_some_function = my_decorator(just_some_function ,4 ,5)

just_some_function(4 ,5)





def my_decorator(some_function1):

    def wrapper1(b ,a):

        print("we want to find sum of " , a , " and ", b)

        some_function1(4 ,5)

        print("is the sum is correct for " , a , " and ", b)
    return wrapper1


def just_some_function(a1 ,b1):
    # print("Wheee!")
    print(a1 + b1)

just_some_function(44 ,55)

just_some_function = my_decorator(just_some_function)

just_some_function(4 ,5)









def decorator2(name="jose"):
    def greet():
        return "This string is inside greet"

    def welcome():
        return "this string is inside welcome"

    if name == "jose":
        return greet
    else:
        return welcome


x = decorator2()  # x = greet
x = decorator2(name ="atul")
print(x())


# -*- coding: utf-8 -*-
"""
Created on Fri Jun  8 11:36:17 2018

@author: atanand
"""

def foo(bar):
    return bar + 1


print(foo(2) == 3)

def foo(bar):
    return bar + 1

print(foo)
print(foo(2))
print(type(foo))





def foo(bar):
    return bar + 1

print(foo)
print(foo(2))
print(type(foo))


def call_foo_with_arg(foo, arg):
    return foo(arg)

print(call_foo_with_arg(foo, 3))







def parent(num):

    def first_child():
        print( "Printing from the first_child() function.")

    def second_child():
        return "Printing from the second_child() function."

    try:
        assert num == 10
        return first_child
    except AssertionError:
        return second_child

foo = parent(10)
bar = parent(11)

print(foo)
print(bar)

print(foo())
print(bar())











import time


def timing_function(some_function):

    """
    Outputs the time a function takes
    to execute.
    """

    def wrapper():
        t1 = time.time()
        some_function()
        t2 = time.time()
        return "Time it took to run the function: " + str((t2 - t1)) + "\n"
    return wrapper


@timing_function
def my_function():
    num_list = []
    for num in (range(0, 999999)):
        num_list.append(num)
        num_list.pop()
        # print(num_list)
    # print("\nSum of all the numbers: " + str((sum(num_list))))


print(my_function())