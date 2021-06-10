# -*- coding: utf-8 -*-
"""
https://www.hackerearth.com/practice/basic-programming/input-output/basics-of-input-output/practice-problems/algorithm/prime-number-8/
"""

'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''

# Write your code here

def isitem_primeNo(item):
    prime = True
    for i in range(2,int((item/2)+1)):
        if item % i ==0:
            prime= False
            return prime
    return prime
        
        


n= int(input())
result=[]
for item in range(2,n):
    if isitem_primeNo(item):
        result.append(item)
        
    else:
        pass
    
result_str="".join(str(result))
print(result_str,type(result_str))    
