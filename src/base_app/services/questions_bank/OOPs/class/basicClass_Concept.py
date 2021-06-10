# -*- coding: utf-8 -*-
"""
Created on Fri Mar 30 18:12:38 2018

@author: atanand
"""

class A:
    a="I am a class attribute !"
    
x=A()
y=A()

print(x.a)
print(y.a)
print(A.a)


x.a="This creats a new instance attribute for x!"
print(y.a)
print(A.a)

A.a="This is changing the class attribute 'a' !"
print(A.a)
print(y.a)
print(x.a)    


class Human:
    population =0
    
    def __init__(self,name):
        self.name=name
        print("My name is ",self.name)
        Human.population  +=1
        
    def __del__(self):
        Human.population -=1
        print("Decrementing the population")
    
    def howMany(self):
        if Human.population ==1:
            print("I am the only one here ")
        else:
            print("There are still {} guys left".format(Human.population))
            print("guys left are:",(Human.population))
            
human1=Human('Atul')
human1.howMany()            
human2=Human('Srishti')
human1.howMany()            
#adya=Human('Adya')
human1.howMany()            