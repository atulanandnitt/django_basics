def heapify(arr,n,i):
    indexOfLargest=i
    l = 2 *i +1
    r = 2*i +2
    
    if l<n and arr[l] > arr[i]:
        indexOfLargest = l
    if r<n and arr[r] > arr[indexOfLargest]:
        indexOfLargest =r
        
    if i != indexOfLargest:
        arr[i],arr[indexOfLargest] = arr[indexOfLargest],arr[i]
        heapify(arr,n,indexOfLargest)
        
def heapSort(arr,k):
    n=len(arr)
    
    for i in range(n//2 -1,-1,-1):
        heapify(arr,0,i)
    for i in range(n-1,k,-1):
        arr[i],arr[0]= arr[0],arr[i]
        heapify(arr,i,0)
        

list1=[5,3,1,2,4]
k=4
heapSort(list1,k)
print(list1)
print(list1[k])
