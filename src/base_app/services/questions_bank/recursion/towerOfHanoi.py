# -*- coding: utf-8 -*-
"""
Created on Sun Nov 11 06:05:44 2018

@author: Atul Anand
"""

#code



def  Hanoi(disk, source, dest, aux):
    if disk == 1:
        print('move disk {} from rod {} to rod {}'.format(disk, source, dest))
        return 1
    else:
        steps = Hanoi(disk - 1, source, aux, dest)
        print('move disk {} from rod {} to rod {}'.format(disk, source, dest))
        steps = steps + 1
        return steps + Hanoi(disk - 1, aux, dest, source)


t = int(input())

for i in range(t):
    nDisks = int(input())

    pilha = list(range(1, nDisks))
    print(Hanoi(nDisks, 1, 3, 2))


    