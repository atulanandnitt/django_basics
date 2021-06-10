# -*- coding: utf-8 -*-
"""
https://practice.geeksforgeeks.org/problems/steps-by-knight/0
"""

from collections import deque

moves = [(1, 2), (2, 1), (1, -2), (2, -1), (-1, 2), (-2, 1), (-1, -2), (-2, -1)] 
def min_jumps(n, src, dst):
    
    board = [[0] * n for _ in range(n)]
    q = deque()
    q.append((src, 0))
    
    while q:
        (i, j), dist = q.popleft()
        if i < 0 or j < 0 or i >= n or j >= n:
            continue
        #print(i, j, dst)
        if (i, j) == dst:
            return dist

        if board[i][j]:
            continue
        board[i][j] = 1
        
        for mi, mj in moves:
            q.append(((i + mi, j + mj), dist + 1))
            
    return 1    
    
import sys
lines = sys.stdin.readlines()

T = int(lines[0].strip())
i = 1
for _ in range(T):
    n = int(lines[i].strip())
    #print(lines[i+1].split())
    src = tuple(int(c)-1 for c in lines[i+1].split())
    dst = tuple(int(c)-1 for c in lines[i+2].split())
    print(min_jumps(n, src, dst))
    i += 3
    
    
    
    
print("""""""""""""""""""""""""""""""""""""""""")
def neighbor(value):
    
    x = value[0]
    y = value[1]
    
    temp = []
    
    temp.append((x + 1, y + 2))
    temp.append((x + 1, y - 2))
    temp.append((x - 1, y + 2))
    temp.append((x - 1, y - 2))
    
    temp.append((x + 2, y + 1))
    temp.append((x + 2, y - 1))
    temp.append((x - 2, y + 1))
    temp.append((x - 2, y - 1))
    
    return temp
    


def knight_steps(n, knight, target):
    
    hash ={}
    visited = set()
    queue =[]
    
    hash[knight] = 0
    queue.append(knight)
    
    while queue:
        
        current = queue.pop(0)
        
        if current == target:
            return hash[target]
        
        if current in visited:
            continue
        visited.add(current)
        
        possibilities = neighbor(current)
        
        for value in possibilities:
            x = value[0]
            y = value[1]
            
            if 0 < x <= n and 0 < y <= n:
                queue.append(value)
                hash[value] = hash[current] + 1
                    
    return 1



t = int(input().strip())
for i in range(t):
    n = int(input().strip())
    knight = tuple(map(int, input().strip().split()))
    target = tuple(map(int, input().strip().split()))
    
    result = knight_steps(n, knight, target)
    print (result)    