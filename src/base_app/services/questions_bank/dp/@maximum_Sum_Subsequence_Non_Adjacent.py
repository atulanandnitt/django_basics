
#https://www.youtube.com/watch?v=UtGtF6nc35g&list=PLrmLmBdmIlpsHaNTPP_jHHDx_os9ItYXr&index=34




def maximum_Sum_Subsequence_Non_Adjacent_simplified(list1):
    solList=[]
    
    for item in list1:
        solList.append(item)
    solList[1]=max(solList[0],solList[1])
    for i in range(2,len(list1)):
        solList[i]=(max(solList[i-2]+list1[i],solList[i-1]))
        #excl[i]=incl[i-1]
    
    print(solList)

list1=[4,1,1,4,2,1]    
maximum_Sum_Subsequence_Non_Adjacent_simplified(list1)    
    



def maximum_Sum_Subsequence_Non_Adjacent(list1):
    incl=[]
    for item in list1:
        incl.append(item)
    #incl[-1]=0
    print("incl :",incl)
    excl=[0 for i in range(len(list1))]
    for i in range(1,len(list1)):
        incl[i]=(max(excl[i-1]+list1[i],incl[i-1]))
        excl[i]=incl[i-1]
    
    print(incl)
    print(excl)
    
    
list1=[4,1,1,4,2,1]    
maximum_Sum_Subsequence_Non_Adjacent(list1)    
