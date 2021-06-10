dict1={'Atul':11,'Anand':22}

print(dict1)

dict1['Atul']=33
print(dict1)


#dict1.clear()
#del dict1
del dict1['Atul']

print(dict1.keys())
print(dict1.values())

print(dict1.items())

list1=[1,1,2,2,2,3,3,3,4,4,4]
dict1={key:list1.count(key) for key in list1}
print(dict1)

