#job scheduling prob:
#https://www.youtube.com/watch?v=cr6Ip0J9izc&index=12&list=PLrmLmBdmIlpsHaNTPP_jHHDx_os9ItYXr

def jobScheduling(list1):
    solList=[]
    for item in list1:
        solList.append(item[1])
    
    for i in range(len(list1)):
        for j in range(0,i):
            #print(list1[i][0][0] , "list1[j][1] : ", list1[j][0][1])
            if list1[i][0][0] >= list1[j][0][1]:#job dont overlaps
               solList[i] = max(solList[i] ,list1[i][1] + solList[j])
            
            
    print(solList)  
    return max(solList)
    
    
    
list1=[[[1,3],5],
       [[2,5],6],
       [[4,6],5],
       [[6,7],4],
       [[5,8],11],
       [[7,9],2]
       ]

print(jobScheduling(list1))    


