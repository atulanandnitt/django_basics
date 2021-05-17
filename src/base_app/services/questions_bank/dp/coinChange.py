

# Dynamic Programming Python implementation of Coin 

# Change problem

#https://www.youtube.com/watch?v=jaNZ83Q3QGc
def noOfWayCoinsCanBeReturned(coins, n, val):
    """    # table[i] will be storing the number of solutions for
    # value i. We need n+1 rows as the table is constructed
    # in bottom up manner using the base case (n = 0)
    # Initialize all table values as 0
    """
    table = [0 for _ in range(val+1)]
    table[0] = 1
    print(coins)
    # Pick all coins one by one and update the table[] values     # after the index greater than or equal to the value of the     # picked coin
    for i in range(0,n):
        for j in range(coins[i],val+1):
            """
            print("table is : ", table)
            print("table[j]",table[j],"j is :",j)
            print("j-S[i] : ",j-coins[i])
            """
            table[j] += table[j-coins[i]]
    print("table :",table)
    return table[val]

coins = [3,5,7]
val=15
n = len(coins)
x = noOfWayCoinsCanBeReturned(coins, n,val)
print (x)

# Recursive Python3 program for
# coin change problem.
 
# Returns the count of ways we can sum
# S[0...m-1] coins to get sum n
def countOfSoluntions(S, m, val ):
 
    # If n is 0 then there is 1
    # solution (do not include any coin)
    if (val == 0):
        return 1
 
    # If n is less than 0 then no
    # solution exists
    if (val < 0):
        return 0;
 
    # If there are no coins and n
    # is greater than 0, then no
    # solution exist
    if (m <=0 and val >= 1):
        return 0
 
    # count is sum of solutions (i) 
    # including S[m-1] (ii) excluding S[m-1]
    #return countOfSoluntions( S, m - 1, val ) + countOfSoluntions( S, m, val-S[m-1] );
    return countOfSoluntions( coins, m - 1, val ) + countOfSoluntions( coins, m, val-coins[m-1] );
 
# Driver program to test above function
coins = [1,2,5,6]
val=12
n = len(coins)
print(countOfSoluntions(coins, n, val))
