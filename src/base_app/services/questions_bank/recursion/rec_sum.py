# -*- coding: utf-8 -*-
"""
Created on Sat Mar 24 11:57:44 2018

@author: atul
"""

#recursion sum:

def rec_sum(n):
    if n:
        return n+rec_sum(n-1)
    else:
        return 0

print(rec_sum(11))


def rec_sum_of_each_individual_nos(n):
    if n/10 ==0:
        return n
    else:
        return n%10 + rec_sum_of_each_individual_nos(n//10)
    
print(rec_sum_of_each_individual_nos(123))




def word_split(phrase,list_of_words,output = None):
    
    if output is None:
        output =[]
        
    for word in list_of_words:
        if phrase.startswith(word):
            output.append(word)
            print("len(word) is : ",len(word),"word is ",word)
            return word_split(phrase[len(word):],list_of_words,output)
    return output


subString = 'ilovedogsJohn'
list_of_words=['i','am','a','dogs','lover','love','John']        

solution=  word_split(subString,list_of_words)
print(solution)


"""
def subStringfun(str):
    subString=[]
    length = len(str)
    i,j=0,0
    while i<length:
        j=i
        while j<length:
            subString.append(str[i:j+1])
            j+=1
        i+=1
    return subString


print(subStringfun("atul"))

def word_split(inputStr,listStr):
    subString=subStringfun(inputStr)
    sol=[]
    for item in listStr:
        if item in subString:
            sol.append(item)
    return sol

print(word_split('themanran',['the','man','ran']))
print(word_split('ilovedogsJohn',['i','am','a','dogs','lover','love','John']))
"""    