#https://practice.geeksforgeeks.org/problems/maximum-tip-calculator/0

t=1#int(input())
for _ in range(t):
    N, X, Y=7, 3, 4#map(int,input().strip().split())
    a=[8,7,5,9,6,6,8]#list(map(int,input().strip().split()))
    b=[1,7,5,1,2,3,9]#list(map(int,input().strip().split()))
    
    c = sorted(zip(a,b), key=lambda p:abs(p[0]-p[1]))
    print(c)
    sum=0
    while N>0:
        if c[-1][0] > c[-1][1]:
            if X >0:
                X -=1
                N -=1
                sum +=  c[-1][0]
            else:
                Y -=1
                N -=1
                sum +=  c[-1][1]
                
        elif c[-1][0] < c[-1][1] :
            if Y>0:
                Y -=1
                N -=1
                sum +=  c[-1][1]
            else:
                X -=1
                N -=1
                sum +=  c[-1][0]
                
        elif c[-1][0] == c[-1][1] :
            if X >Y :
                X =-1
                N -=1
                sum +=  c[-1][0]
            else:
                Y -=1
                N -=1
                sum +=  c[-1][1]
        print(sum,X,Y)
        c=c[:-1]
    
    print(sum)

str1="atul"
subStr=[str1[i:j+1] for i in range(len(str1)) for j in range(i,len(str1))]

for i in range(len(str1)) :
    for j in range(i,len(str1)):
        print(str1[i:j+1])
print(subStr)
"""
list1=[1,2,3,4,5]
print(sum(list1))

import itertools
list1=[1,2,3,4,5]
for tup in itertools.combinations(list1,3):
    print(tup)

#print(sum(list1))


"""




"""
Created on Thu May  3 19:17:43 2018
5 3 3
1 2 3 4 5
5 4 3 2 1
@author: atanand
"""
"""
t=1#int(input().strip())
while t:
    n,x,y=4,3,3#map(int,input().strip().split(' '))
    a=[1,2,3,4,5]#list(map(int,input().strip().split(' ')))
    b=[5,4,3,2,1]#list(map(int,input().strip().split(' ')))
    c=sorted(zip(a,b), key=lambda p: abs(p[0]-p[1]))
    print("c is :", c)
    count=0
    c=c[::-1]
    #print(c)
    for i,j in c[0:n]:
        if y==0:
           count+=i
           x-=1
        elif x==0:
            count+=j
            y-=1
        elif i>j:
            count+=i
            x-=1
        elif i<j:
            count+=j
            y-=1
        elif i==j:
            if x>y:
                count+=i
                x-=1
            else:
                count+=j
                y-=1
        print("inside the for loop :",count)
    print (count)
    t-=1
"""