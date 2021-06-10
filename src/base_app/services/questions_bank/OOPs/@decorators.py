def my_decorator(some_function,a,b):

    def wrapper():

        print("Something is happening before some_function() is called.")

        some_function(a, b)

        print("Something is happening after some_function() is called.")

    return wrapper


def functionNeedsDecorator_1(a, b):
    print("inside real function")
    print("a+b", a+b)


a, b = 1, 2
functionWithDecorator = my_decorator(functionNeedsDecorator_1, a, b)

functionWithDecorator()






def my_decorator(fun1):

    def wrapper1():
        print("prefix")
        fun1()
        print("Something is happening after some_function() is called.")

    return wrapper1


# functionNeedsDecorator = my_decorator(functionNeedsDecorator)
@my_decorator
def functionNeedsDecorator():
    print("in side the real funtion")

functionNeedsDecorator()


"""

def my_decorator(fun2, c, d):

    def wrapper1():
        print("prefix")
        fun2(c,d)
        print("Something is happening after some_function() is called.")

    return wrapper1


# functionNeedsDecorator = my_decorator(functionNeedsDecorator)
@my_decorator(c, d)
def functionNeedsDecorator(c, d):
    print("c: ", c, "d : ", d)
    print("in side the real funtion")

functionNeedsDecorator(4,5)

"""