# -*- coding: utf-8 -*-
"""
Created on Fri Oct 26 20:49:03 2018

@author: Atul Anand
"""

import itertools
def find_2_num_summing_to_x(list1,x):
    for t1 in itertools.combinations(list1,2):
        if t1[0] + t1[1] ==x:
            return 1
    else:
        return 0
    
    
list1=[1,2,3,9]
x=10   
print(find_2_num_summing_to_x(list1,x))    