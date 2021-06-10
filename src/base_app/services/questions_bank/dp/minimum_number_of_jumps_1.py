# -*- coding: utf-8 -*-
"""
Created on Fri Oct 26 22:17:31 2018

@author: Atul Anand
"""

#code

def minimum-number-of-jumps(a,N):
    dp = [float('inf') for x in range(N)]
    dp[0] = 0
    for i in range(N):
        for j in range(i):
            if j + a[j] >= i:
                dp[i] = min(dp[i], dp[j] + 1)
    
    if dp[-1] == float('inf'):
        print(-1)
    else:
        print(dp[-1])
        


N = int(input())

for _ in range(N):
    list1 = list(map(int, input().split()))        
    N = len(list1)
    findSolution(list1,N)  