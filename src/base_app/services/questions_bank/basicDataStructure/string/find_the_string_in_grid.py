# -*- coding: utf-8 -*-
"""
Created on Tue Jul 10 14:16:13 2018

@author: atanand
"""

#code
def find_the_string_in_grid(n,m,grid,word,x,y):
    for dx in [-1,0,1]:
        for dy in [-1,0,1]:
            if not (dx == 0 and dy == 0):
                match = True
                for i in range(len(word)):
                    if 0 <= x + i*dx and x + i*dx < m and 0 <= y + i*dy and y + i*dy < n:
                        if word[i] != grid[y+i*dy][x+i*dx]:
                            match = False
                            break
                    else:
                        match = False
                if match:
                    return True

T = 1#int(input())
for t in range(T):
    n,m = (3,3)#tuple(map(int, input().split()))
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']#input().split()
    grid = [letters[i*m:(i+1)*m] for i in range(n)]
    word = "abc"#input()
    results = set()
    for x in range(m):
        for y in range(n):
            if find_the_string_in_grid(n,m,grid,word,x,y):
                results.add((y,x))

    if not results:
        print('-1')
    else:
        for c in sorted(list(results)):
            print(str(c[0]) + ' ' + str(c[1]), end=', ')
        print('')



tupple1=(1,2,3)
tupple1[0]=6
print(tupple1[0])



     
        
        