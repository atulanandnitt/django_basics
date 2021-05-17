
import itertools

def out(n, arr, x):
	if(n<4):
		return 0
    
	for tup in itertools.combinations(arr, 4):
      
		if(sum(tup)==x):
			return 1
    
	return 0

t =1# int(input())
for m in range(t):
    n = 6#int(input()) #no use of n in python
    list1 =[1,5,1,0,6,0]# [int(x) for x in input().split()]
    print(list1,type(list1))
    x = 7#int(input())
    print(out(n, list1, x))
    print("atul",itertools.combinations(list1, 4))
    for tup in itertools.combinations(list1, 4):
        print("tup is ", tup, "type(tup)", type(tup))
        


#code

import itertools

def findSol(tupple1,val):
    solStr=""
    if sum(tupple1) == val:
        for item in tupple1:
            solStr += str(item)
            solStr += " "
        return solStr
    else:
        pass

t=int(input())

for _ in range(t):
    n,val=map(int,input().strip().split()) # no of items in the input list
    #val=int(input())
    map1 = map(int,input().strip().split())
    list1=list()
    for item in map1:
        list1.append(item)
    list1.sort()
    sol=""
    tempSol=""
    for tup in itertools.combinations(list1,4):
        tempSol = findSol(tup,val)
        if tempSol:
            sol += tempSol 
            sol +="$"
    if sol is "":
        print (-1)
    else:
        print(sol)
    

"""
sample i/p:
    1

    6
    
    1 5 1 0 6 0
   
    7

output:    1

"""    