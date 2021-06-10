#code
#https://practice.geeksforgeeks.org/problems/largest-square-formed-in-a-matrix/0/?ref=self

def largest_square_formed_in_a_matrix(l,m,n):
    a = []
    now = 0
    for i in range(m):
        a.append(l[now : now + n])
        now += n
    
    dp = [[0 for i in range(n)] for j in range(m)]
    
    for i in range(0, m):
	    for j in range(0, n):
		    if i == 0 or j == 0:
			    dp[i][j] = a[i][j]
		    elif a[i][j] == 0:
			    dp[i][j] = 0
		    else:
			    dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1]) + 1
    ans = 0
    for i in dp:
	    t = max(i)
	    ans = max(ans, t)
    return (ans)



t =1# int(input())

for _ in range(t):
    m, n = 5,6# [int(i) for i in input().split(" ")]
    list1 = [0,1,0,1,0,1,1,0,1,0,1,0,0,1,1,1,1,0,0,0,1,1,1,0,1,1,1,1,1,1]#[int(i) for i in input().strip().split(" ")]
    print(largest_square_formed_in_a_matrix(list1,m,n))
    
"""
3
5 6
0 1 0 1 0 1 1 0 1 0 1 0 0 1 1 1 1 0 0 0 1 1 1 0 1 1 1 1 1 1
2 2
1 1 1 1
2 2
0 0 0 0
"""    