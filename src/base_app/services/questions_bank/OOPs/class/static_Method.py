# -*- coding: utf-8 -*-
"""
Created on Fri Mar 30 18:51:42 2018

@author: atanand
"""

class A(object):
    
    def method(self,x): #method can be called by object only
        print("aam")
        print("executing method(%s,%s"%(self,x))
        
    @classmethod
    def class_method(cls,x):#class method can be called by both a:object of the class and b:class itself
        print("Executing class_method(%s,%s)"%(cls,x))
    
    @staticmethod#static method can be called by both a:object of the class and b:class itself.
                    # behaves like plan function,execpt that it can be called by 
                    #used to group functions which have connections within.
    def static_method(x):
        print("executing static_method(%s)"%x)
        print("executing static_method{}".format(x))
        
a=A()    
a.method(1)


#calling class method using class and object
a.class_method(1)    
A.class_method(1)


a.static_method(1)