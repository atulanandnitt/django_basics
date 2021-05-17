# -*- coding: utf-8 -*-
"""
neither call by value nor call by reference
"""

#List is mutable

def change_list_contents(the_list):
    print("got",the_list)
    the_list.append('Four')
    print("chagned to",the_list)
    
outer_list=['one','two','three']

print('before, outer_list',outer_list)
change_list_contents(outer_list)
print('after, outer_list',outer_list)
print(" ****************LIST IS MUTABLE")



def change_tupple_contents(the_tupple):
    print("got",the_tupple)
    temp_tupple=('four',)
    the_tupple =the_tupple+ temp_tupple
    print("chagned to",the_tupple)
    
outer_tupple=('one','two','three')

print('before, outer_tupple',outer_tupple)
change_tupple_contents(outer_tupple)
print('after, outer_tupple',outer_tupple)
print("**************************TUPPLE IS IMMUTABLE")


def change_list_reference(the_list):
    print('got',the_list)
    the_list=['and','we','cant','lie']
    print('set to',the_list)
    
outer_list =['we','like','proper','english']

print('before,outer_list :',outer_list)
change_list_reference(outer_list)
print('after ,outer_list =',outer_list)



def change_str_reference(the_str):
    print('got',the_str)
    the_str="I am the modifed str"
    print('set to',the_str)
    
outer_str ="original string"

print('before,outer_str :',outer_str)
change_str_reference(outer_str)
print('after ,outer_str =',outer_str)



def change_int_reference(the_int):
    print('got',the_int)
    the_int=99999
    print('set to',the_int)
    
outer_int =1

print('before,outer_int :',outer_int)
change_int_reference(outer_int)
print('after ,outer_int =',outer_int)