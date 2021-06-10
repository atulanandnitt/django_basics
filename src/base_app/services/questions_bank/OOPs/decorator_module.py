

def my_decorator(some_function):

    def wrapper1(num):

        #num = 10

        if num == 10:
            print("Yes! val of num is 10")
        else:
            print("No!  val of num is NOT 10")

        some_function()

        print("Something is happening after some_function() is called.")

    return wrapper1


if __name__ == "__main__":
    my_decorator()
    
