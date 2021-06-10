

def find_0_1_knapsack_problem3(totalCapacity, weights, values):
    n=len(values)
    dp = [[0 for j in range(totalCapacity+1)]for i in range(n+1)]
    
    for i in range(0,n+1):
        for j in range(0,totalCapacity+1):
            if i==0 or j==0:
                dp[i][j]=0
                continue
            
            if(weights[i-1]<= j):
                dp[i][j] = max(values[i-1]+dp[i-1][j-weights[i-1]],dp[i-1][j])
            else:
                dp[i][j] = dp[i-1][j]

    return dp[-1][-1]
    
    
def find_0_1_knapsack_problem(totalCapacity, weights, values):
    n=len(values)
    dp = [[0 for j in range(totalCapacity+1)]for i in range(n+1)]
    
    for i in range(0,n+1):
        for j in range(0,totalCapacity+1):
            if i==0 or j==0:
                dp[i][j]=0
                continue
            
            if(weights[i-1]<= j):
                dp[i][j] = max(values[i]+dp[i-1][j-weights[i]], dp[i-1][j])
            else:
                dp[i][j] = dp[i-1][j]

    return dp[-1][-1]    

    
t =1# int(input())

for _ in range(t):
    
    waste = 3#int(input())
    totalCapacity = 4#int(input())
    values = [1,2,3]#list(map(int, input().strip().split()))
    weights = [4,5,1]#list(map(int, input().strip().split()))
    print(find_0_1_knapsack_problem3(totalCapacity,values,weights))
