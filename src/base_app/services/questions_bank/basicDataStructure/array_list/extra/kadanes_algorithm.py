#code


def kadanes_algorithm2(list1):
    tempSum=0
    maxTillNow =0
    for i in range(len(list1)):

        if tempSum < 0:
            if tempSum-list1[i] >0:
                maxTillNow = max(maxTillNow, tempSum-list1[i])
                print("maxTillNow :", maxTillNow)
                tempSum =0
                continue
            else:
                tempSum =0
                continue
        
        tempSum += list1[i]
        maxTillNow = max(maxTillNow, tempSum)
        print("outside   maxTillNow :", maxTillNow)
    
    if maxTillNow ==0:
        return -1
    else:    return maxTillNow
    
    
    
def kadanes_algorithm1(list1):
    tempSum=0
    maxTillNow =0
    for i in range(len(list1)):

        if list1[i] < 0:

            maxTillNow = max(maxTillNow, tempSum)
            tempSum =0
            continue
        
        tempSum += list1[i]
        maxTillNow = max(maxTillNow, tempSum)
    
    if maxTillNow ==0:
        return -1
    else:    return maxTillNow


def kadanes_algorithm3(list1):
    tempSum=0
    maxTillNow =0
    for i in range(len(list1)):

        if tempSum < 0:

            maxTillNow = max(maxTillNow, tempSum-list1[i])
            tempSum =0
            continue
        
        tempSum += list1[i]
        maxTillNow = max(maxTillNow, tempSum)
    
    if maxTillNow ==0:
        return -1
    else:    return maxTillNow
                

t = 1#int(input())
for _ in range(t):
    waste = 1#int(input())
    list1 = [1,2,-8,3,-9,-2,-2,5,-3]#list(map(int, input().strip().split()))
    #list1=[-1,-2,-3,-4]
    #print(kadanes_algorithm1(list1))
    #print(kadanes_algorithm2(list1))
    print(kadanes_algorithm3(list1))