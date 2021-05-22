
class Sorting:

    def __init__(self, arr):
        self.arr = arr

    def heapify(self, n, i):
        index_of_largest = i
        l = 2*i +1
        r = 2 * i + 2
        if l < n and self.arr[index_of_largest] < self.arr[l]:
            index_of_largest = l
        if r < n and self.arr[index_of_largest] < self.arr[r]:
            index_of_largest = r

        if index_of_largest != i:
            self.arr[i], self.arr[index_of_largest] = self.arr[index_of_largest], self.arr[i]
            self.heapify(n,index_of_largest)
    
    def heap_sort(self):
        n = len(self.arr)
        for i in range(n//2 -1, -1, -1):
            self.heapify(n,i)

        for i in range(n-1, 0, -1):
            self.arr[i], self.arr[0] = self.arr[0], self.arr[i]
            self.heapify(n,i)
        
        return self.arr
    

arr = [5,4,6,3,7,2,8,1,9,10]
s1 = Sorting(arr)
print(s1.heap_sort())