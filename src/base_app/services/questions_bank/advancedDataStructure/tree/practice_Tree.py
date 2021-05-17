class Sort:
    def __init__(self, arr):
        self.arr = arr
        self.n = len(arr)

    def heapify(self,n,i):
        index_of_largest = i
        l = 2*i +1
        r = 2*i+2
        if l < n and self.arr[index_of_largest] < self.arr[l]:
            index_of_largest = l
        if r<n and self.arr[index_of_largest] < self.arr[r]:
            index_of_largest = r
        
        if index_of_largest != i:
            self.arr[i], self.arr[index_of_largest] = self.arr[index_of_largest], self.arr[i]
            self.heapify(n,i)
    
    def heap_sort(self):
        for i in range(self.n//2, -1, -1):
            self.heapify(self.n,i)
        
        for i in range(self.n-1, -1, -1):
            self.arr[0], self.arr[i] = self.arr[i], self.arr[0]
            self.heapify(i, 0)
        return self.arr
        

arr = [5,4,6,3,7,2,8,1,9,111]
s = Sort(arr)
print(s.heap_sort())
