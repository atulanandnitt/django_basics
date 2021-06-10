# -*- coding: utf-8 -*-
"""
Created on Fri Mar 30 19:21:53 2018

@author: atanand
"""

strList=[1,2,3,4,5,6,7,8,9,10]
[item **2 for item in strList]

square_listComprehension=[i**2 for i in range(11)]
print(square_listComprehension)

squareLambdaFunciton = lambda x:x**2
print(squareLambdaFunciton(10)) #print(squareLambdaFunciton(range(10))) range not supported

list1=range(11)
MultipliedList=[item*3 for item in list1]
print(MultipliedList)

inputStr="atul"
allSubStr=[inputStr[i:j+1] for i in range(len(inputStr))  for j in range(i,len(inputStr))]
print(allSubStr)


inputList=['atul','srishti','anshu']
firstLetter=[item[0] for item in inputList]
print(firstLetter)

str1="Hello 1234 word"
numFromStr=[x for x in str1 if x.isdigit()]
print(numFromStr)

digitSet={1,2,3,4,5,6,7,8,9,0}
numFromStr=[x for x in str1 if x in digitSet]
print("numFromStr",numFromStr)









for item in str1:
    pass
    #print(item)

list1=str1.strip().split()
for item in list1:
    print(item) 
    
reverse=[]    
for i in range(len(list1)):
    reverse.append(list1[len(list1) -1 -i])
    
print(reverse)    