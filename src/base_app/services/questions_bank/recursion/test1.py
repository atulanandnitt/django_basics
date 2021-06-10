#cache
n=111
cache=[None]*(n+1)     #cache=[]....whats the issue ????
def fib_dyn(n):
    
    #base Case
    if n==0 or n==1:
        return 1
    
   
    
    try:
        return cache[n]
    except:
        cache[n] = fib_dyn(n-1) + fib_dyn(n-2)
        return cache[n]

print("fib_dyn")
for i in range(111): #less than n
    print(i,"  " ,fib_dyn(i))