# -*- coding: utf-8 -*-
"""
Created on Wed Jun  6 14:00:42 2018

@author: atanand
"""


class Driver:
    def __init__(self):
        pass
    
    def defineDriver(self,D_id,name):
        self.D_name = name
        self.D_id = D_id
        self.avg_D_rating =0
        
d = [0 for i in range(11)]
for i in range(11):
    d[i] = Driver()
    d[i].defineDriver(i,str("Driver"+chr(ord("A") +1)))
    d[i].avg_D_rating = (10+i)
"""
if driverObj.D_id == 5:
    print(driverObj)
"""
print(d[5].D_id) 
print(d[5].avg_D_rating) 
print(c[5].cus_id) 
print(c[5].avg_C_rating)
  

class Customer:
    def __init__(self):
        pass
    
    def defineCustomer(self,C_id,name):
        self.cus_name = name
        self.cus_id = C_id
        self.avg_C_rating =0


c = [0 for i in range(11)]
for i in range(11):
    c[i] = Customer()
    c[i].defineCustomer(i,"Customer"+chr(ord("A") +1))
    c[i].avg_C_rating = (100+i)

print(c[5].cus_id) 
print(c[5].avg_C_rating)

