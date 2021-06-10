

def removeDuplicates(str1):
    list1=[]
    for item in str1:
        list1.append(item)

    dict1={key:list1.count(key) for key in set(list1)}
    print(dict1,type(dict1))

    values=[values1 for (keys1,values1) in dict1.items()]
    print(values)
    
    keys=[keys1 for (keys1,values1) in dict1.items()]
    print(keys)
    keys_str="".join(keys)
    print(keys_str)
    
str1="FOLLOW UP"
removeDuplicates(str1)
    