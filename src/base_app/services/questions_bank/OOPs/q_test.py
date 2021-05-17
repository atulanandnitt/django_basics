#q_test
import p_main

def f_main(self):
    print("inside q_test")
    


f_main=p_main.MyClass.f
obj = p_main.MyClass
obj.f(0) 

"""

p_main.MyClass.f=f_main
obj = p_main.MyClass
obj.f(0)    

"""