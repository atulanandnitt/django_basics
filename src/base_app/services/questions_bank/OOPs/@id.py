
print("deaf {x1} and {x2}".format(x1='abc', x2='bcd' ))




class Count:
    def __init__(self, count =0):
        self.__count = count
    

c1 = Count(2)
c2 = Count(2)

print(id(c1) == id(c2), end=" ")

s1 = "Good"
s2 = "Good"

print(id(s1) == id(s2))
print(s1 , s2)
s1="bad"
print(s1 , s2)
print(id(s1) == id(s2))


print(id(c1))