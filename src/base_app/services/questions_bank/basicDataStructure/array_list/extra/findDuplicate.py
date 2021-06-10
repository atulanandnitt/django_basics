list1=[4,5,3,6,2,8,1,5,4,65,43,6,5,6]

dict1={ key: list1.count(key) for key in list1}

for key,val in dict1.items():
    if val >2:
        print(key)
