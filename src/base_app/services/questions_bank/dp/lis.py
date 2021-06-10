def dp_lis(list1):
    lis=[1 for _ in range(len(list1))]
    
    for i in range(len(list1)):
        for j in range(0,i):
            if arr[i] > arr[j] and lis[i] < lis[j] +1:
                lis[i] = lis[j] +1
    
    lengthOfMaxIncSubSeq = max(lis)
    return lengthOfMaxIncSubSeq


list1=[10 , 22 , 9 , 33 , 21 , 50 , 41 , 60]
print("max length is : ",dp_lis(list1))











# A naive Python implementation of LIS problem
 
""" To make use of recursive calls, this function must return
 two things:
 1) Length of LIS ending with element arr[n-1]. We use
 max_ending_here for this purpose
 2) Overall maximum as the LIS may end with an element
 before arr[n-1] max_ref is used this purpose.
 The value of LIS of full array of size n is stored in
 *max_ref which is our final result """
 
# global variable to store the maximum
global maximum
 
def _lis(arr , n ):
 
    # to allow the access of global variable
    global maximum
 
    # Base Case
    if n == 1 :
        return 1
 
    # maxEndingHere is the length of LIS ending with arr[n-1]
    maxEndingHere = 1
 
    """Recursively get all LIS ending with arr[0], arr[1]..arr[n-2]
       IF arr[n-1] is maller than arr[n-1], and max ending with
       arr[n-1] needs to be updated, then update it"""
    for i in range(1, n):
        res = _lis(arr , i)
        if arr[i-1] < arr[n-1] and res+1 > maxEndingHere:
            maxEndingHere = res +1
 
    # Compare maxEndingHere with overall maximum. And
    # update the overall maximum if needed
    maximum = max(maximum , maxEndingHere)
 
    return maxEndingHere
 
def lis(arr):
 
    # to allow the access of global variable
    global maximum
 
    # lenght of arr
    n = len(arr)
 
    # maximum variable holds the result
    maximum = 1
 
    # The function _lis() stores its result in maximum
    _lis(arr , n)
 
    return maximum
 
# Driver program to test the above function
arr = [10 , 22 , 9 , 33 , 21 , 50 , 41 , 60]
n = len(arr)
print ("Length of lis is ", lis(arr))
 
# This code is contributed by NIKHIL KUMAR SINGH


# Dynamic programming Python implementation of LIS problem
 
# lis returns length of the longest increasing subsequence
# in arr of size n
def lis(arr):
    n = len(arr)
 
    # Declare the list (array) for LIS and initialize LIS
    # values for all indexes
    
    #lis = [1]*n
    lis =[1 for _ in range(n)]
    # Compute optimized LIS values in bottom up manner
    for i in range (1 , n):
        for j in range(0 , i):
            if arr[i] > arr[j] and lis[i]< lis[j] + 1 :
                lis[i] = lis[j]+1
 
    # Initialize maximum to 0 to get the maximum of all
    # LIS
    maximum = 0
    print("max val is : ",max(lis))
    # Pick maximum of all LIS values
    for i in range(n):
        maximum = max(maximum , lis[i])
 
    return maximum
# end of lis function
 
# Driver program to test above function
arr = [10, 22, 9, 33, 21, 50, 41, 60]
print ("Length of lis is", lis(arr))
# This code is contributed by Nikhil Kumar Singh
