def decorator1(myFun1):
    
    def myFun2():
        print("prefix ")
        myFun1()
        print("postfix")
    return myFun2

@decorator1
def sum2Nos():
    print("summing to number")
    
sum2Nos() 



def decorator2(name="jose"):
    def greet():
        return "This string is inside greet"
    
    def welcome():
        return "this string is inside welcome"

    if name == "jose":
        return greet
    else:
        return welcome


x = decorator2()  # x = "greet" 
x = decorator2(name ="atul")
print(x())    