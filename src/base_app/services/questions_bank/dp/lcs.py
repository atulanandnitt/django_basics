#LCS



def lcs2(X,Y,m,n):
    if m==0 or n ==0:
        return 0
    
    elif X[m-1] ==Y[n-1]:
        return 1 + lcs2(X,Y,m-1,n-1)
    
    else:
        return max(lcs2(X,Y,m-1,n) , lcs2(X,Y,m,n-1))
    


X = "AGGTAB"
Y = "GXTXAYB"
print("length : ",lcs2(X,Y,len(X),len(Y)))






# A Naive recursive Python implementation of LCS problem
 
def lcs(X, Y, m, n):
 
    if m == 0 or n == 0:
       return 0;
    elif X[m-1] == Y[n-1]:
       return 1 + lcs(X, Y, m-1, n-1);
    else:
       return max(lcs(X, Y, m, n-1), lcs(X, Y, m-1, n));
 
 
# Driver program to test the above function
X = "AGGTAB"
Y = "GXTXAYB"
print ("Length of LCS is ", lcs(X , Y, len(X), len(Y)))

