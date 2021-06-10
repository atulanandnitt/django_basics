# -*- coding: utf-8 -*-
"""
Created on Sat Mar 17 14:59:35 2018

@author: atul
"""

#string compression

def stringCompression(inputStr):
    #inputList=inputStr.strip().split()
    inputList=[]
    for item in inputStr:
        inputList.append(item)
    strDicCount = dict([(key,inputList.count(key)) for key in inputList])
    
    print(strDicCount)
    """
    output1="".join(strDicCount.keys)
    output2="".join(strDicCount.values())
    i=0
    for item in output1:
        print(output1[i],output2[i])
        i +=1
    """
    
inputStr ="AAAABBBBBBCCCCCCC"
stringCompression(inputStr)    



def compress(s):
    
    r =""
    l=len(s)
    
    if l==0:
        return ""
    
    if l ==1:
        return s+"1"
    
    last = s[0]
    cnt = 1
    i=1
    
    while i<l:
        
        if s[i] == s[i-1]:
            cnt +=1
        else:
            r=r+s[i-1] + str(cnt)
            cnt =1
        i +=1
        
    r = r+s[i-1] +str(cnt)
    
    return r

inputStr ="AAAABBBBBBCCCCCCC"
compress(inputStr)             