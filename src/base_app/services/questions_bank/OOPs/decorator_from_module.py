from decorator_module import my_decorator

@my_decorator
def just_some_function():
    print("in side the real funtion")
    
just_some_function(10)    