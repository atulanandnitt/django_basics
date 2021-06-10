# -*- coding: utf-8 -*-
"""
Created on Fri Mar 30 18:31:56 2018

@author: atanand
"""

#findTheNoOfInstancesOfClass

def get_no_of_instances(cls_obj):
    return cls_obj.count

class SampleClass:
    count =0
    
    def __init__(self):
        SampleClass.count+=1 #???? why not self.count +=1
        #return self.count
    

ik1=SampleClass()
ik2=SampleClass()

print(get_no_of_instances(SampleClass))    