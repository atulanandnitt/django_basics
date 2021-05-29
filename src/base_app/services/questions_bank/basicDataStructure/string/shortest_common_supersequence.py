# -*- coding: utf-8 -*-
"""
Created on Mon Jul  2 18:15:55 2018

@author: atanand
"""

#code

def shortest_common_supersequence(str1,str2):
    list1,list2=[],[]
    solVal =0
    str1=str1.strip()
    str2=str2.strip()
    for chr1 in str1:
        list1.append(chr1)
    print("list1 :",list1)
    dict1={key:list1.count(key) for key in set(list1)}
    print(dict1)
    for chr1 in str2:
        list2.append(chr1)
    dict2={key:list2.count(key) for key in set(list2)}    
    print(dict2)
    solDic=dict1
    
    for key,value in dict2.items():
        if key not in dict1.keys():
            solDic[key] = value
        else:
            solDic[key] = max(value, solDic[key])
    
    print("solDic :",solDic)
    for key,value in solDic.items():
        solVal += value
        

    return solVal
    

str1="nablhvsjmriftxjrlhnszricvabvwibl"
str2="jeysbrenimubjfvwmionbypwysuwbxkm"

print(shortest_common_supersequence(str1,str2)    )









"""
def shortest_common_supersequence(str1,str2):
    list1,list2=[],[]
    for chr1 in str1:
        list1.append(chr1)
        
    for chr1 in str2:
        list2.append(chr1)
        
    set1=set(list1)
    set2=set(list2)
    
    solSet=set2
    for item in set1:
        solSet.add(item)
    
    
    return len(solSet)
    
t=int(input())

for _ in range(t):
        
    str1,str2 =input().split()
    
    
    print(shortest_common_supersequence(str1,str2)    )
"""