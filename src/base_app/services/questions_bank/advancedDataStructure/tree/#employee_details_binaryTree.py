# -*- coding: utf-8 -*-
"""
Created on Wed Apr  4 20:40:53 2018

@author: atanand
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Apr  4 20:17:06 2018

@author: atanand
"""

import time

class Node:
    def __init__(self,val):
        for i in range(len(val)):
            print(val[i])
        
        self.name_Data=val[0]
        self.empId_data=val[1]
        self.seatNo_data=val[2]
        self.left=None
        self.right=None
        #self.reportee=val[3]#generic multi child tree


def findEmp_seatNo(seatNo):
    root.level=0
    temp_level=root.level
    temp_list=[root]
    bfs_list=[]
    print("bfs_list",bfs_list)
    while len(temp_list) >0:
        temp = temp_list.pop(0)
        
        if temp.level > temp_level:
            temp_level +=1
        
        bfs_list.append(temp.name_Data)
        
        #print("temp.empId_data : ",temp.empId_data , "seatNo : ",seatNo)
        if temp.seatNo_data == seatNo:
            return temp.name_Data,temp.empId_data
        
        if temp.left:
            temp.left.level = temp_level +1
            temp_list.append(temp.left)
            
        if temp.right:
            temp.right.level = temp_level +1
            temp_list.append(temp.right)
            
    print(bfs_list)


def find_parent_of_emp(empId):
    root.level=0
    root.parent=None
    temp_level=root.level
    temp_list=[root]
    bfs_list=[]
    print("bfs_list",bfs_list)
    print("empId : ",empId)
    while len(temp_list) >0:
        temp = temp_list.pop(0)
        
        if temp.level > temp_level:
            temp_level +=1
        
        bfs_list.append(temp.name_Data)
        
        #print("temp.empId_data : ",temp.empId_data , "empId : ",empId)
        if temp.empId_data == empId:
            return temp.parent.empId_data
        
        if temp.left:
            temp.left.level = temp_level +1
            temp_list.append(temp.left)
            temp.left.parent=temp
            
        if temp.right:
            temp.right.level = temp_level +1
            temp_list.append(temp.right)
            temp.right.parent=temp
            
    #print(bfs_list)

def find_emp_node(empId):
    root.level=0
    temp_level=root.level
    temp_list=[root]
    bfs_list=[]
    #print("bfs_list",bfs_list)
    while len(temp_list) >0:
        temp = temp_list.pop(0)
        
        if temp.level > temp_level:
            temp_level +=1
        
        bfs_list.append(temp.name_Data)
        
        #print("temp.empId_data : ",temp.empId_data , "seatNo : ",seatNo)
        if temp.empId_data == empId:
            return temp
        
        if temp.left:
            temp.left.level = temp_level +1
            temp_list.append(temp.left)
            
        if temp.right:
            temp.right.level = temp_level +1
            temp_list.append(temp.right)
            
    print(bfs_list)
    
    
def findPath(empId):
    root.level=0
    root.parent=None
    temp_level=root.level
    temp_list=[root]
    
    parentList=[]

    while len(temp_list) >0:
        temp = temp_list.pop(0)
        
        if temp.level > temp_level:
            temp_level +=1
        
        if temp.empId_data == empId:
           while temp.parent is not None:
                    parentList.append(temp.parent.empId_data)
                    temp=temp.parent
                    
                    if temp.parent is root:
                        parentList.append(temp.parent.empId_data)
                        return parentList
                        

        
        if temp.left:
            temp.left.level = temp_level +1
            temp_list.append(temp.left)
            temp.left.parent=temp
            
        if temp.right:
            temp.right.level = temp_level +1
            temp_list.append(temp.right)
            temp.right.parent=temp
    
    print ("parentList :  " ,parentList)
    

    
def findPathBetweenTwoNodes(empId1,empId2):#empId2 is one of the parents of empId1
    root.level=0
    root.parent=None
    temp_level=root.level
    temp_list=[root]
    
    parentList=[find_emp_node(empId1).empId_data]
    empId2_node=find_emp_node(empId2)
    while len(temp_list) >0:
        temp = temp_list.pop(0)
        
        if temp.level > temp_level:
            temp_level +=1
        
        if temp.empId_data == empId1:
           while temp.parent is not empId2_node:
                    parentList.append(temp.parent.empId_data)
                    temp=temp.parent
                    
                    if temp.parent is root:
                        parentList.append(temp.parent.empId_data)
                        return parentList
                        

        parentList=[find_emp_node(empId2).empId_data]
        if temp.left:
            temp.left.level = temp_level +1
            temp_list.append(temp.left)
            temp.left.parent=temp
            
        if temp.right:
            temp.right.level = temp_level +1
            temp_list.append(temp.right)
            temp.right.parent=temp
    
    print ("parentList :  " ,parentList)

    
def findEmployee_org_relationship(input_empId1,input_empId2):
    input_empId1_node=find_emp_node(input_empId1)
    input_empId2_node=find_emp_node(input_empId2)
    
    parentList1=findPath(input_empId1)
    parentList2=findPath(input_empId2)
    print("parentList1  : ",parentList1)
    print("parentList2  : ",parentList2)
    solList=[input_empId1]

    
    for item in parentList1:
        if item in parentList2:
            #solList.append(item) 
            #for item2 in parentList2:
            #   solList.append(item2)
            #solList.pop()
            try:
                solList.append(findPathBetweenTwoNodes(input_empId1_node,input_empId2_node))
            
            except:
                pass            
            break
        else:
            solList.append(item) 
    solList.append(input_empId2)       
    print("findEmployee_org_relationship : ",solList)
    return solList
    
root=Node(["SVP",1,101])
vp1=Node(["vp1",2,102,["d1","d2"]])

vp2=Node(["vp2",3,103,["d5","d6"]])

root.left=vp1
root.right=vp2


d1=Node(["d1",4,104,["M1"]])
d2=Node(["d2",5,105,["M2","M3"]])
d5=Node(["d5",8,108,["M6","M7"]])
d6=Node(["d6",9,109,["M8","M9"]])

vp1.left=d1
vp1.right=d2

vp2.left=d5
vp2.right=d6


print(vp1.left.name_Data)

seat=104
print("employee Name, emp ID of a person seating at seat no : ",seat,findEmp_seatNo(seat))


empId=9
print("employee ID of parent of a employee having employee ID: ",empId," is : ",find_parent_of_emp(empId))

empId1=4
print("employee ID of parent of a employee having employee ID: ",empId1," is : ",find_parent_of_emp(empId1))

print("findPath for ",empId1, " : ",findPath(empId1))

time.sleep(1)

empId2=9
print("employee ID of parent of a employee having employee ID: ",empId2," is : ",find_parent_of_emp(empId2))

print("findPath for ",empId2, " : ",findPath(empId2))

print("****************************************************")
empId1=4
print("findPath for ",empId1, " : ",findPath(empId1))
empId2=5
print("findPath for ",empId2, " : ",findPath(empId2))

print("relationship : ",findEmployee_org_relationship(empId1,empId2))

print("****************************************************")
empId1=4
print("findPath for ",empId1, " : ",findPath(empId1))
empId2=9
print("findPath for ",empId2, " : ",findPath(empId2))

print("relationship : ",findEmployee_org_relationship(empId1,empId2))


print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")

print(findPathBetweenTwoNodes(4,2))