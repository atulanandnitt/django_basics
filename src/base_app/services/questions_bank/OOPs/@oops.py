list1 = [3,4,5,20,5,25,1,3]
list1.pop()
list1.pop(1)
print(list1)


l =[1,23,'hello',1]
print(l,type(l))


class Person():
    def __init__(self):
            
        self.firstname = "Foo"
        self.lastname = "Bar"
        self._phonenumber ="0"
    
    #@property  # causing error "TypeError: 'str' object is not callable"
    def fullname(self):
        return self.firstname + " " + self.lastname
    
    #@property
    def phone(self):
        return self._phonenumber

    #@phone.setter
    def phone(self, value):
        if len(value) != 10:
            raise ValueError("Invalid Phone number")
        self._phonenumber = value

p = Person()
print(p.fullname())


class Demo:
    def __init__(self):
        self.x =1 
        print("from base class")
    
    def change(self):
        self.x =10
        
        
class Demo_derived(Demo):
    def __init__(self):
        self.x =11
        print("from __init__ parent class")
    
    def change(self):
        print("from parent class 1")
        self.x=self.x +1
        print("from parent class 2")
        return self.x
    
def main():
    obj = Demo_derived()
    print(obj.change())
    
main()    
        


def mk(x):
    def mk1():
        print("Decorated")
        x()
    return mk1


def mk2():
    print("Ordinary")
    
p = mk(mk2)
p()    



def summation(a,b,*args):
    return a+b+sum(args)

print(summation(1,2,3,4,5,6))


def summarion2(a,b,**kwargs):
    val = a+b
    print("kwargs :", kwargs)
    for item in kwargs:
        #val += int(item)
        print(item,type(item))
    for key1,val1 in kwargs.items():
        val += val1
        
    return val

print(summarion2(1,2,c=3,d=4,e=5,f=6,g=7))


def testgen(index):
    weedays =['sun','mon','tue','wed','thu','fri','sat']
    yield weedays[index]
    yield weedays[index+1]

day = testgen(0)
for i in range(3):
    print(next(day))


A0 = {'a':1, 'c':3, 'b':2, 'e':5, 'd':4}
A1 = range(10)
A2 = sorted([i for i in A1 if i in A0])
A3 = sorted([A0[s] for s in A0])
A4 = [i for i in A1 if i in A3]
A5 = {i: i*i for i in A1}
A6 = [[i, i*i] for i in A1]

print(A0)
print(A1)
print(A2)
print(A3)
print(A4)
print(A5)
print(A6)





        
    