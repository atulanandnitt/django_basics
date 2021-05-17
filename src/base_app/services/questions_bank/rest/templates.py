from string import Template

class MyTemplate(Template):
    delimiter = '#'

def Main():
    cart = []
    cart.append(dict(item='Coke', price=8, qty=1))
    cart.append(dict(item='Cake', price=12, qty=2))
    cart.append(dict(item='Fish', price=22, qty=4))

    t = MyTemplate("#price * #qty = #price")
    total = 0
    print(cart)

    for data in cart:
        print(t.substitute(data))
        total += data["price"]

    print("total " + str(total))

def summation(a,b,*args,**kwargs):
    result = a+b
    for item in args:
        result += int(item)

    for key1, val1 in kwargs.items():
        result += int(val1)
    print("p is ", kwargs['p'])
    print("kwargs",kwargs, type(kwargs))
    print("args", args, type(args))
    return result

if __name__ == "__main__":
    Main()
    print(summation(1,2,3,4,5,p=1,q=2,r=4))
