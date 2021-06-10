class MathCal(object):

    def __init__(self,dataA,dataB):
        self.valA=dataA
        self.valB = dataB
        print(self)

    def summation(self):
        return self.valA + self.valB


mathObj = MathCal(1,2)

print(mathObj.summation())


class Employee:

    num_of_emps =0
    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.pay = pay

        Employee.num_of_emps += 1


    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)


    #class method example: without self
    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amt = amount



emp_1 = Employee('Atul','Anand',5000)
emp_2 = Employee('Atul','Anand',6000)


print(Employee.raise_amt)
print(emp_1.raise_amt)
print(emp_2.raise_amt)





class MathCal2(object):
    num_of_emps = 0
    def __init__(self):
        self.valA=0
        self.valB = 0

        MathCal2.num_of_emps += 1

    def summation(self, dataA, dataB):
        self.valA=dataA
        self.valB = dataB
        return self.valA + self.valB

    def countOfInstances():
        return MathCal2.num_of_emps


mathObj2 = MathCal2()

print(mathObj2.summation(1,2))


mathObj3 = MathCal2()

print(mathObj2.summation(11,22))


mathObj4 = MathCal2()

print(mathObj2.summation(100,200))

print( MathCal2.num_of_emps)


print(MathCal2.countOfInstances())