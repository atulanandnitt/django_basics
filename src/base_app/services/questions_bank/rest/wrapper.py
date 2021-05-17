def addition(fun1):
    
    def my_wrapper():
        print("my name is Atul")
        
        fun1()
        print("Anand")
        
    return my_wrapper
        
def fun2():
    print("inside the exact funtion")
        
fun3=addition(fun2)   
fun3()

def my_decorator(some_function):

    def wrapper():

        print("Something is happening before some_function() is called.")

        some_function()

        print("Something is happening after some_function() is called.")

    return wrapper


def just_some_function():
    print("Wheee!")


just_some_function = my_decorator(just_some_function)

just_some_function()





def my_decorator(some_function):

    def wrapper():

        print("Something is happening before some_function() is called.")

        some_function()

        print("Something is happening after some_function() is called.")

    return wrapper


def just_some_function():
    print("Wheee!")



@wrapper
just_some_function()



a=10
is_instance(obj)



x=[1,2,3]
y=[4,5,6]
z=[1,2,3]
print(id(x))
print(id(y))
print(id(z))
print(id(x) == id(z))

print(a is_identical)

print(1 is 1)
print('2' is '1')