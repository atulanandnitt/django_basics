
def find_Mini_dif(list1):
    tempDif=0
    minDiffTillNow= 999
    sublist=[list1[i:j] for i in range(len(list1)) for j in range(i+1,len(list1))]
    subList2 =[]
    for i in range(len(list1)):
        for j in range(i+1,len(list1)):
            subList2.append(list1[i:j])
            tempDif =  abs(sum(list1[i:j]) - sum(list1[:i]+list1[j:]))
            minDiffTillNow = min(minDiffTillNow,tempDif)
            print("minDiffTillNow :" ,minDiffTillNow, "tempDif :", tempDif ,i,j, sum(list1[i:j]), sum(list1[:i]+list1[j:]))
    
    
    print(minDiffTillNow)


import itertools

def find_Mini_dif2(list1):
    tempDif=0
    minDiffTillNow= 999
    for i in range(len(list1)):
        for t1 in itertools.combinations(list1,i):
            tempList =
            tempDif =  abs(sum(t1) - sum(list1[:i]+list1[j:]))




t = 1#int(input())
for _ in range(t):
    n = 4#int(input())
    #list1 = [1,6,5,11]#list(map(int, input().strip().split()))
    list1=[20,21,19,9]
    print(find_Mini_dif(list1))
    print(find_Mini_dif2(list1))