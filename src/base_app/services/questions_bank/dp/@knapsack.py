"""
Given weights and values of n items, put these items in a knapsack of capacity W to get the maximum total value in the knapsack.

https://practice.geeksforgeeks.org/problems/0-1-knapsack-problem/0

"""





values=[2,2,4,5]
weights=[2,4,6,9]
totalWt=8

values=[1,3,4,5]
weights=[1,4,5,7]
totalWt=7


values=[15,10,9,5]
weights=[1,5,3,4]
totalWt=8

print(knapsack(totalWt,weights,values)) 


#code
def find_0_1_knapsack_problem2(totalWt, wt, val):
    n=len(values)
    dp = [[0 for j in range(totalWt+1)]for i in range(n+1)]
    
    for i in range(0,n+1):
        for w in range(0,totalWt+1):
            if i==0 or w==0:
                dp[i][w]=0
                continue
            
            if(wt[i-1]<=w):
                dp[i][w] = max(val[i-1]+dp[i-1][w-wt[i-1]],dp[i-1][w])
            else:
                dp[i][w] = dp[i-1][w]

    return dp[n][w]


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
    

# what issue 2    
def find_0_1_knapsack_problem(totalCapacity, weights, values):
    n=len(values)
    dp = [[0 for j in range(totalCapacity+1)]for i in range(n+1)]
    
    for i in range(0,n+1):
        for j in range(weights[i],totalCapacity+1): # why its wrong !!!!
            if i==0 or j==0:
                dp[i][j]=0
                continue
            
            if(weights[i]<= j):
                dp[i][j] = max(values[i]+dp[i-1][j-weights[i]],dp[i-1][j])
            else:
                dp[i][j] = dp[i-1][j]

    return dp[-1][-1]    
    
def knapsack2(totalWt, wt, val):#whats the issue???
    #n=len(values)
    dp = [0 for i in range(totalWt+1)]
    
    for i in range(1,totalWt+1):
        for j in range(1,len(wt)):#j is wt index
            dp[i] = max(val[j]+dp[i-wt[j]],dp[i])

    print(dp)
    return dp[totalWt]

def knapsack2(totalWt, wt, val):#whats the issue???
    #n=len(values)
    dp = [0 for i in range(totalWt+1)]
    
    for i in range(1,totalWt+1):
        for j in range(1,len(wt)):#j is wt index
            dp[i] = max(val[j]+dp[i-wt[j]],dp[i])

    print(dp)
    return dp[totalWt]

values=[1,10,4,5]
weights=[1,5,3,4]
totalWt=18

print("knapsack2 :", knapsack2(totalWt,weights,values)) 



values=[15,10,9,5]
weights=[1,5,3,4]
totalCapacity=8

print(knapsack(totalCapacity,weights,values)) 
#print(find_0_1_knapsack_problem(totalCapacity,weights,values))
print(find_0_1_knapsack_problem2(totalCapacity,weights,values))
print(find_0_1_knapsack_problem3(totalCapacity,weights,values))
#print(knapsack2(totalCapacity,weights,values))    
