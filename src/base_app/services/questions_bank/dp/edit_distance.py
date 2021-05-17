# -*- coding: utf-8 -*-
"""
Created on Sat Oct 27 10:30:57 2018

@author: Atul Anand
"""

def min_op (n, m, str1, str2) :
    op = [[i+j for i in range(n+1)] for j in range(m+1)]
    print(op)
    for i in range(m) :
        for j in range(n) :
            if str1[j] == str2[i] :
                op[i+1][j+1] = op[i][j]
            else :
                op[i+1][j+1] = min(op[i][j+1], op[i+1][j], op[i][j]) + 1
    print(op[-1][-1])
    print(str1)
    print(str2)
    print(op)
    
    
t = 1#int(input())
for i in range(1) :
    L =[4,5]# [int(i) for i in input().split(" ")]
    str1,str2 = "geek","gesss"#input().strip().split()
    min_op (L[0], L[1], str1, str2)
    