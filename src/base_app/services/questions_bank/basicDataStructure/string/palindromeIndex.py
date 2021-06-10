# -*- coding: utf-8 -*-
"""
Created on Wed May 23 12:44:08 2018

@author: atanand
"""

#https://www.hackerrank.com/challenges/palindrome-index/problem

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the palindromeIndex function below.


def isPalindrome(s,i):
    s2=""
    for j in range(len(s)):
        if j != i:
            s2 += s[j]
        else:
            continue
    length = len(s2)
    for i in range(length):
        if s2[0] == s2[length -1]:
            continue
        else:
            return False
    return True
    
    
def palindromeIndex(s):
    length = len(s)
    counter =0
    for i in range(length):
        if s[0] == s[length -1]:
            counter += 1
            continue
        else:
            break
    if counter == length:
        return -1


    for i in range(len(s)):
        if isPalindrome(s,i):
            return i
    return -1

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = 1#int(input())

    for q_itr in range(q):
        s = "aaab"#input()
        s="baa"
        s="aaa"

        result = palindromeIndex(s)

        print(result)