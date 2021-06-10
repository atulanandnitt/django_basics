
def create_max_heap(arr, n, i):
    index_of_largest = i
    l = 2*i +1
    r= 2*i+2
    if l<n and arr[index_of_largest] < arr[l]:
        index_of_largest = l
    if r<n and arr[index_of_largest] < arr[r]:
        index_of_largest = r

    if index_of_largest != i:
        arr[index_of_largest], arr[i] = arr[i], arr[index_of_largest]
        create_max_heap(arr, n, i)
    # if r>n:
    #     return arr

def max_heap(arr):
    sol = create_max_heap(arr, len(arr), 0)
    print("sol", sol)
    print("arr", arr)

arr= [1111,4,3,5,6,2,7,1,9,11,111]
max_heap(arr)