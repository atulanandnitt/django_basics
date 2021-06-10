

#code

def find_padovan_sequence(n):
    if n ==0 or n ==1 or n==2:
        return 1
    else:
        return find_padovan_sequence(n-2) + find_padovan_sequence(n-3)

def dp_find_padovan_sequence(n):
    if n ==0 or n ==1 or n==2:
        return 1
    else:
        
        prevprev, prev, curr, nextp = 1, 1, 1, 1
        for j in range(3,n+1):
            nextp = prevprev+prev
            prevprev = prev
            prev = curr
            curr = nextp
    return nextp

    
    
            


t =1# int(input())
for _ in range(t):
    n = 12#int(input())
    #print(find_padovan_sequence(n))
    print(dp_find_padovan_sequence(n))
    
    
    
def fibo(n):
    a,b=0,1
    if n==1:
        return 0
    elif n==2:
        return 1

    for i in range(2,n):
        a,b = b,a+b
    return b

for i in range(1,11):
    print(fibo(i))
    
    
def all26(str1):
    dict1 = {key1:str1.count(key1) for key1 in set(str1)}
    allKey=dict1.keys()
    allAlpha="abcdefghijklmnopqrstuvwxyz"
    for chr1 in allAlpha:
        if chr1 in allKey:
            continue
        else:
            return False
    else:
        return True
    

str1="abcdefghijklmnopqrstuvwxyzdggerg34645y"
print(all26(str1))    