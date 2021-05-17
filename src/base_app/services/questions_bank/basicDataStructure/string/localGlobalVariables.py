a=2                       #Global Variable
def add():
    b=3                       #Local Variable
    # global a=10 SyntaxError: invalid syntax
    global a
    a = 10
    c=a+b
    a = 10# UnboundLocalError: local variable 'a' referenced before assignment
    print("local a",a)
    print(c)
add()
print("global a",a)


list1= ['atul','anand','srishti','atul']
list1.remove('atul')
print("after removing atul ",list1)
list1.remove('atul')
print("after removing atul 2nd time ",list1)
list1.pop(1)
list1.pop(1)