

def longest_bitonic_subsequence(list1):
    lis_fromLeft=[1 for item in range(len(list1))]    
    lis_fromRight=[1 for item in range(len(list1))]    
    lds=[1 for item in range(len(list1))]    
    bitonic_list=[1 for item in range(len(list1))]    
    for i in range(len(list1)):
        for j in range(i):
            if list1[i] > list1[j]:
                lis_fromLeft[i] = max(lis_fromLeft[i] , lis_fromLeft[j] +1)
    print("lis_fromLeft" ,lis_fromLeft)
    
    for i in range(len(list1)-1,-1,-1):
        for j in range(len(list1)-2,0,-1):
            if list1[i] > list1[j]:
                lis_fromRight[i] = max(lis_fromRight[i],lis_fromRight[j]+1)
    print("lis_fromRight ",lis_fromRight)
    
    for i in range(len(list1)):
        for j in range(i):
            if list1[i] < list1[j]:
                lds[i] = max(lds[i] , lds[j] +1)
    print("lds" ,lds)
    
    
    for i in range(len(lis_fromLeft)):
        bitonic_list[i] = lis_fromLeft[i] + lis_fromRight[i] -1
    
    print("bitonic_list",bitonic_list)
    return max(bitonic_list)
list1=[31,64,97,58,14,21,84,47,45,90,37,27,35,71,52,12,82,82,75,100,83,46,86,6,34,77,57,96,35,57,3,17,72,51,74,37,24,10,83,68,99,19,94,33,42,46,44,75,79,70,75,61,68,60,66,1
]
print(longest_bitonic_subsequence(list1))     