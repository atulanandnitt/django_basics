#code

def findNoOfWays(list1,val):
    count=0
    list2=[]
    for item in list1:
        list2.append(item)
    for i in range(len(list1)):
        for j in range(i+1,len(list1)):
            #for k in range(j+1,len(list1)):
            print("count :",count,"list1 :",list1)
            try:
                x=list1[i]
                y=list1[j]
                list1.remove(list1[i])
                list1.remove(list1[j])
                mini=min(list1)
                if ((val - x -y ) > mini):
                   count += 1
                   print("count :",count,"list1 modified :",list1,"mini :",mini)
            except:
                continue
        for item in list2:
            list1.append(item)
    return count
            
            

t= 1# int(input())

for _ in range(t):
    waste,val=5,12#map(int,input().strip().split())
    list1=[5,1,4,3,7]#list(map(int,input().strip().split()))
    
    print(findNoOfWays(list1,val))
    
"""    
list1=[5,1,4,3,7]#list(map(int,input().strip().split()))
print(min(list1[3:]))
print(list1.remove(5))
print(list1)
"""