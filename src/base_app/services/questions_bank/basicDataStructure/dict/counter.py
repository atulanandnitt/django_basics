# -*- coding: utf-8 -*-
"""
Created on Wed Oct 31 11:17:53 2018

@author: Atul Anand
"""


from collections import Counter

def main():
    
    fruitList1 =['apple','pear','orange','banana','apple','grape']
    
    fruitList2 =['apple','pear','orange','banana','grape','carrot']
    
    c1 =Counter(fruitList1)
    
    c2 =Counter(fruitList2)
    
    print(c1["apple"])
    
    print(sum(c1.values())) #print(sum(c1.keys()))
    
    print(c1.most_common()) #print(c1.most_common(3))
    
    print(c1 & c2) #only common, a kind of intersection
    
main()    