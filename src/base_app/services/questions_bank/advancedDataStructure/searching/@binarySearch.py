

def binarySearchRecursive(list1,k):

    if len(list1) == 0:
        return False
    else:
        mid = len(list1) //2
        print("list1 is :",list1, "mid is ",mid)
        
        if list1[mid] == k:
            return True
        
        if list1[mid] < k:
            return binarySearchRecursive(list1[mid+1:],k)
            
        else:
            return binarySearchRecursive(list1[:mid],k)
        
        
list1=[1,2,3,4,5,6,7,8,9]
k=2
if (binarySearchRecursive(list1,k)):
    print(k ,"found in ",list1)
else:
    print("not found in binarySearchRecursive")    
    
    

print("binarySearchIterative")
def binarySearchIterative(list1,k):
    
    start=0
    end = len(list1) -1
    found = False
    while start <= end and found is False:
        mid = (start + end ) //2
        if list1[mid] == k:
            found = True
            print("found")
            return True
        else:
            if k < list1[mid]:
                end=mid-1
            else:
                start =mid+1
    return False
        
list1=[1,2,3,4,5,6,7,8,9]
k=5
if (binarySearchIterative(list1,k)):
    print(k ,"found in ",list1)
else:
    print("not found")    
                