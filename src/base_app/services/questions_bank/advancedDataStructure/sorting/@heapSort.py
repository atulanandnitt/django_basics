# -*- coding: utf-8 -*-
"""
Created on Tue Sep 25 00:37:39 2018

@author: Atul Anand
"""

# Python program for implementation of heap Sort
 
# To heapify subtree rooted at index i.
# n is size of heap

class Sorting:
    
    def __init__(self, arr):
        self.arr = arr
        self.n = len(arr)

    def heapify(self, n, i):#maxHeap
        indexOfLargest = i # Initialize indexOfLargest as root
        l = 2 * i + 1     # left = 2*i + 1
        r = 2 * i + 2     # right = 2*i + 2
    
        # See if left child of root exists and is
        # greater than root
        if l < n and self.arr[i] < self.arr[l]:
            indexOfLargest = l
    
        # See if right child of root exists and is
        # greater than root
        if r < n and self.arr[indexOfLargest] < self.arr[r]:
            indexOfLargest = r
    
        # Change root, if needed
        if indexOfLargest != i:
            self.arr[i], self.arr[indexOfLargest] = self.arr[indexOfLargest], self.arr[i] # swap
    
            # Heapify the root.
            self.heapify(n, indexOfLargest)
    
    # The main function to sort an array of given size
    def heapSort(self):
        # Build a maxheap.
        for i in range(self.n//2 -1, -1, -1):
            self.heapify(self.n, i)
            print("after heapify arr :", arr)
    
        # One by one extract elements
        for i in range(self.n-1, 0, -1):
            arr[i], arr[0] = arr[0], arr[i] # swap
            self.heapify(i, 0)
            print("****arr :",arr)
        return arr

     
 
# Driver code to test above
arr = [5,300,1,2,4]
s1 = Sorting(arr)
sol = s1.heapSort()
n = len(sol)
print ("Sorted array is")
for i in range(n):
    print ("%d" %sol[i], end=", "),
# This code is contributed by Mohit Kumra
