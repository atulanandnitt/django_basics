class Employee:

    num_of_emps = 0
    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        #self.email = first + '.' + last + '@email.com'
        self.pay = pay


        Employee.num_of_emps += 1

    #getter and setter method
    #inbuild decorator @property used to
    #define as a function but access like a variable(instance variable in this case)
    @property
    def email(self):
        return "{}.{}@gmail.com".format(self.first, self.last)

    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    @fullname.setter
    def fullname(self, name):
        self.first, self.last = name.split()


    @fullname.deleter
    def fullname(self):
        self.fullname = None


    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

    def __repr__(self):#by default implemented to return the address of the instance of the class
        if self.first:
            return "Employee('{}','{}','{}')".format(self.first, self.last, self.pay)
        else:
            return "No employee found"

    def __str__(self):
        return '{} - {}'.format(self.fullname, self.email)

    def __add__(self, other):
        return self.pay + other.pay

    def __len__(self):
        return 10 * len(self.first)



    @classmethod
    def set_raise_amt(cls1, amount):
        cls1.raise_amt = amount


class Developer(Employee):
    #raise_amt = 1.10

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        # Employee.__init__(self, first, last, pay)
        self.prog_lang = prog_lang


class Manager(Employee):

    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emp(self):
        for emp in self.employees:
            print('-->', emp.fullname)


emp_1 = Employee('Atul', 'Anand', 5000)
emp_2 = Employee('Atul', 'Anand', 6000)


print(Employee.raise_amt)
print(emp_1.raise_amt)
print(emp_2.raise_amt)

dev_1 = Developer('Atul1', 'Anand1', 50001, 'python1')
dev_2 = Developer('Atul2', 'Anand2', 50002, 'python2')

print(dev_1.pay)
dev_1.apply_raise()
print("updated pay is : ", end="")
print(dev_1.pay)


print(dev_1.email)

mgr_1 = Manager('m1_1', 'm1_2', 90000, [dev_1, dev_2])

print(mgr_1.email)


mgr_1.print_emp()
mgr_1.remove_emp(dev_1)
mgr_1.print_emp()


mgr_1.add_emp(dev_1)
print("all reportee of the manager")
mgr_1.print_emp()

print(isinstance(mgr_1, Developer))
print(isinstance(mgr_1, Manager))
print(issubclass(Developer, Manager))
print(issubclass(Manager, Developer))


print(emp_1)
print(emp_1.__str__())
print(str(emp_1))


print(emp_1)
print(emp_1.__repr__())
print(repr(emp_1))


print(emp_1 + emp_2)

print(emp_1.first, len(emp_1))


print(emp_1.email)
emp_1.first = 'AtiSri'
print(emp_1.email)

emp_1.fullname = 'Srishti Anand'
print(emp_1.email)


del emp_1.fullname
#print(emp_1) ???? how to handle this error
