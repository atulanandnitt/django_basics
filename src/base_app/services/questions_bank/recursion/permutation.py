# -*- coding: utf-8 -*-
"""
Created on Sat Mar 24 19:15:13 2018

@author: atul
"""

def permute(s):
    print("s is : ",s)
    out =[]
    #Base Case
    if len(s) ==1:
        out =[s]
    
    else:
        #for every letter in string
        for i,let in enumerate(s):
            #for every permutation resulting from step2  and step3
            print("i is : ",i)
            for perm in permute (s[:i] + s[i+1:] ):
                
                print ('perm is', perm)
                print ('current letter is', let)
                #add it to the output
                out += [let+perm]
    return out

print(permute("123"))


my_list = ['apple', 'banana', 'grapes', 'pear']
for c, value in enumerate(my_list, 1):
    print(c, value)
    

my_list = ['apple', 'banana', 'grapes', 'pear']
counter_list = list(enumerate(my_list, 1))
print(counter_list)
# Output: [(1, 'apple'), (2, 'banana'), (3, 'grapes'), (4, 'pear')]    



def details():
    my_str = 'apple banana'
    for c, value in enumerate(my_str):
        print(c, value) 
        
    my_str = 'apple banana'
    for c, value in enumerate(my_str, 1):
        print(c, value)    
        
            
    my_str = 'apple banana'
    for c, value in enumerate(my_str, 2):
        print(c, value)        

#print(details())        