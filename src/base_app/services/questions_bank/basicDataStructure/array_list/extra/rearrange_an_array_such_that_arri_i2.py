

def rearrange_an_array_such_that_arri_i2(list1):
    i=0
    l=len(list1)
    while i<l:
        
        for j in range(len(list1)):
            #temp = list1.pop(i)
            if list1[j] == i:
                list1.insert(i,list1.pop(j))
                break
        else:
            list1.insert(i,-1)
        i += 1
        print("in while :", list1)
    list1 =list1[:l]
    solStr = ""
    for item in list1:
        solStr += str(item) + " "
    return solStr.strip()   
    
    
def rearrange_an_array_such_that_arri_i(list1):
    list2=[]
    for i in range(len(list1)):
        if i in list1:
            list2.append(i)
        else:
            list2.append(-1)
    solStr = ""
    for item in list2:
        solStr += str(item) + " "
    return solStr.strip()        
    

t = 1#int(input())

for _ in range(t):
    waste = 1#int(input())
    list1 = [-1,-1,6,1,9,3,2,-1,4,-1]#list(map(int, input().strip().split()))
    print(list1)
    print(rearrange_an_array_such_that_arri_i2(list1))