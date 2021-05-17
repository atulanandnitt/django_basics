# -*- coding: utf-8 -*-
"""
Created on Fri Jun  8 14:07:06 2018

@author: atanand
"""

def my_decorator(fun1):
    def wraper():
        print("before the actual fun")
        fun1()
        print("after the actual fun")
    return wraper

  
    
@my_decorator
def fun1():
    print("inside the fun1()") 


fun1()    


def my_decorator(fun1):
    def wraper(a,b):
        print("before the actual fun")
        fun1(a,b)
        print("after the actual fun")
    return wraper

def fun2(a,b):
    print("inside fun2",a+b)
    
fun2=my_decorator(fun2)
fun2(3,4)    