# -*- coding: utf-8 -*-
"""
Created on Mon Apr  2 11:29:25 2018

@author: atanand
"""



da = {'a': 1, 'b': 2, 'c': 3, 'e': 7}
db = {'a': 4, 'b': 5, 'c': 6, 'd': 9}
d1=dict()
dc = set(da) & set(db)
print(dc)

for i in dc:
  print (i,da[i],db[i])

for i in dc:
  d1[i]=min(da[i],db[i])
  
print("  d1 :::: ",d1)  
  
def makeStrIdentical(str1,str2): # if string has only alphaNumeric
    alphaNumeric=['a','b','c','d','e','f','1','2','3','4','5','6']
    list1=[]#str1.strip().split()
    list2=[]#str2.strip().split()
    
    for item in str1:
        list1.append(item)
        
    for item in str2:
        list2.append(item)
    print("list1 : ",list1)
    print("list2 : ",list2)
    dict1=dict([(key,list1.count(key)) for key in alphaNumeric])
    #dict1.sort(key=lambda y:key )
    dict2=dict([(key,list2.count(key)) for key in alphaNumeric])
    dict5=set(dict3) & set(dict4)
    print("dict5 : ",dict5)
    dict6=dict()     
    for i in dict5:
        print(i)
    

    dict3=sorted(dict1.items(), key=lambda s: s[0])
    dict4=sorted(dict2.items(), key=lambda s: s[0])
    print("dict3 : ",dict3)
    print("dict4 : ",dict4)
    dict5=set(dict3) & set(dict4)
    print("dict5 : ",dict5)
    dict6=dict()     
    for i in dict5:
        print(i)
        #dict6[i]=min(dict3[i] , dict4[i])
    
    print("dict5",dict5)
    print("dict6",dict6)
    """
    print(dict1)
    print(dict2)
    print(dict3)
    print(dict4)
    """
    
str1="aaaaabcd"
str2="abbbbcdd"

makeStrIdentical(str1,str2)
    
    