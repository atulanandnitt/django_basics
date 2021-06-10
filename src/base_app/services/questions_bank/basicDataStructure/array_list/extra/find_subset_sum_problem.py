
def find_subset_sum_problem(a):
    if sum(a)%2 == 1:
        print("1")
        return ('NO')
        
    dp = [[None for i in range((sum(a)//2) + 1)] for j in range(n+1)]
    def subsetSum(a,dp,n,total):
        if dp[n][total] is None:
            if total == 0:
                dp[n][total] = True
            elif n == 0 and total != 0:
                dp[n][total] = False
            elif total < a[n-1]:
                dp[n][total] = subsetSum(a,dp,n-1,total)
            elif total >= a[n-1]:
                dp[n][total] = subsetSum(a,dp,n-1,total) or subsetSum(a,dp,n-1,total-a[n-1])
        return dp[n][total]
    if subsetSum(a,dp,n,sum(a)//2):
        print("2")
        return ('YES')
    else:
        print("3")
        return ('NO')



def subsetSum(a,dp,n,total):
    print(a,dp,n,total)
    if dp[n][total] is None:
        if total == 0:
            dp[n][total] = True
        elif n == 0 and total != 0:
            dp[n][total] = False
        elif total < a[n-1]:
            dp[n][total] = subsetSum(a,dp,n-1,total)
        elif total >= a[n-1]:
            dp[n][total] = subsetSum(a,dp,n-1,total) or subsetSum(a,dp,n-1,total-a[n-1])
    return dp[n][total]

t = 1#int(input())
for _ in range(t):
    #n = int(input())
    #a = [1,5,11,5]#list(map(int,input().split()))
    a = [1,5,11,4,1]#list(map(int,input().split()))
    n = len(a)
    if sum(a)%2 == 1:   
        print('NO')
        continue
    dp = [[None for i in range((sum(a)//2) + 1)] for j in range(n+1)]

    if subsetSum(a,dp,n,sum(a)//2):
        print('YES')
    else:
        print('NO')
        
        
t=1
for _ in range(t):
    n = 1#int(input())
    list1 = [1,5,11,5]#list(map(int,input().split()))
    print(find_subset_sum_problem(list1))
    