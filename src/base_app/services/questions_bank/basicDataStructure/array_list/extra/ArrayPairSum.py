# -*- coding: utf-8 -*-
"""
Created on Fri Mar 16 15:25:16 2018

@author: atul
"""


def pair_sum_order_n(arr,k):
    
    if len(arr) <2:
        return
    
    #Sets for tracking
    seen = set()
    solSet =set()
    
    for num in arr:
        target = k -num
        #target is the compliment for num in arr
        if target not in seen:
            seen.add(num)
            print("seen  *****  ",seen)
        else:
            #output.add(((min (num,target)),max(num,target)))
            solSet.add((num,target))
    print ('\n'.join(map(str,list(solSet))))
    return len(solSet)
        

#print(pair_sum_order_n([1,3,2,2],4))
#print(pair_sum_order_n([1,9,2,8,3,7,4,6,5,5,13,14,11,13,-1],10))

print(pair_sum_order_n([1,2,3,1],5))





"""
# order O(n^2)
def pair_sum(arr,k):
    i,j=0,0
    n=len(arr)
    solList=[]
    #for item in arr:
    
    while i<n:
        j =i+1
        while  j<n:
            
            if (arr[i] + arr[j] ==k) :
                #solList.append(tupple(item,arr[j]))
                solList.append([arr[i],arr[j]])
            else:
                pass
            
            j +=1
        i +=1
        
    #print(solList)
    return len(solList)



print(pair_sum([1,3,2,2],4))
print(pair_sum([1,9,2,8,3,7,4,6,5,5,13,14,11,13,-1],10))

print(pair_sum([1,2,3,1],3))

"""