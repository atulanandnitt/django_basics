# -*- coding: utf-8 -*-
"""
Created on Fri Mar 30 18:45:34 2018

@author: atanand
"""

class SampleClass(object):
    count=0
    
    def __init__(self):
        SampleClass.count +=1
        
    @classmethod
    def get_no_of_instance(cls_obj):
        return cls_obj.count
    
obj1=SampleClass()
obj2=SampleClass()


print(obj1.get_no_of_instance())
print(obj2.get_no_of_instance())
print(SampleClass.get_no_of_instance())    