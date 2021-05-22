"""
a='1'
b=2
print(int(a)+b)

letters=["a","b","c","d","e","f","g","h","i","j"]
print(letters[1])
print(letters[3:6])
print(letters[:3])
print(letters[-2])
print(letters[-3:])
print(letters[0:9:2])

print(list(range(1,21)))

list1=range(1,21)
print(list(list1))
for i in range(len(list1)):
 print(list1[i]*10)
"""
 
"""
list1=range(1,21)
print(list(list1))
list2=[]
for i in range(len(list1)):
    list2.append(str(list1[i]))
   
print(list2)
 """
a=["1",1,"1",2]
a=list(set(a))
print(a)

d={"a":1,"b":2}
print(d)
print(d["b"])

print(d["a"]+d["b"])
d["c"]=3
print(d)