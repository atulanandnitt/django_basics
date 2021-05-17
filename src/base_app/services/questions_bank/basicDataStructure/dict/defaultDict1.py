# -*- coding: utf-8 -*-
"""
Created on Wed Oct 31 11:12:27 2018

@author: Atul Anand
"""

from collections import defaultdict

def main():
    
    fruits =['apple','pear','orange','banana','apple','grape']
    
    #fruitCounter = defaultdict(int)

    fruitCounter = defaultdict(lambda : 100)

    
    for fruit in fruits:
        fruitCounter[fruit] += 1
        
        
    print(fruitCounter)
    
main()    