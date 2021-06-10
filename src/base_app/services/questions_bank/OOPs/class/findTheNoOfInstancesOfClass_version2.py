# -*- coding: utf-8 -*-
"""
Created on Fri Mar 30 18:37:26 2018

@author: atanand
"""

def iget_no_of_instances(ins_obj):
    return ins_obj.__class__.count

class SampleClass(object):
    count =0
    
    def __init__(self):
        SampleClass.count+=1 #???? why not self.count +=1
        #return self.count
    

ik1=SampleClass()
ik2=SampleClass()

print(iget_no_of_instances(ik1))   