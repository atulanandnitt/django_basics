#heap


from heapq import heappush,heappop,heapify

heaplist=[]
nums=[12,3,-2,6,4,8,9]

for num in nums:
    heappush(heaplist,num)
    
while heaplist:
    print(heappop(heaplist))
    print("heap",heaplist)

heapify(nums)
print(nums)

def sortHeap():
    pass
"""

l=len(nums)
for _ in range(l):
    print("atul :",heappop(heap))


l=len(nums)    
for _ in range(l):
    heapify(nums)
    print(heappop(heap))
"""
#print(nums)