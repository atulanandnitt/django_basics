#sum(n)

import itertools

list1=[1,2,3,4,5]
print(itertools.permutations(list1,3))
combo=(itertools.permutations(list1,3))
for item in combo:
    print(item)
    
print("*******combinations********")    
combo=(itertools.combinations(list1,3))
for item in combo:
    print(item)    