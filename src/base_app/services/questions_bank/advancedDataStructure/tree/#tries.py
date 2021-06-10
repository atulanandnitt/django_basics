

import time

class Node:
    def __init__(self,val):
        for i in range(len(val)):
            print(val[i])
        
        self.name_Data=val[0]
        self.empId_data=val[1]
        self.seatNo_data=val[2]
        if len(val)>3:
            self.reportee=val[3:]
        else:
            self.reportee=list()
            
        
        #self.reportee=val[3]#generic multi child tree
class Tree:
    
    def __init__(self):
        self.root = None
        
    def findSeatNo_data(self,name_val):
        tempQ =[self.root]
        # why this raising issue, but the same thing is working incase of @@bst_bft
        self.root.level =0
        tempLevel = self.root.level
        
        while len(tempQ)>0:
            temp = tempQ.pop(0)
            
            if temp.level > tempLevel:
                print("level changed")
                tempLevel += 1
            
            if temp.name_Data == name_val:
                return temp.seatNo_data
            
            if temp.reportee:
                for item in temp.reportee:
                    tempQ.append(item)
            


d1=Node(["d1",4,104,["M1"]])
d2=Node(["d2",5,105,["M2","M3"]])
d5=Node(["d5",8,108,["M6","M7"]])
d6=Node(["d6",9,109,["M8","M9"]])
d7=Node(["d7",8,108,["M10","M11","M12"]])
d8=Node(["d8",9,109,["M13","M14","M15"]])




root=Node(["SVP",1,101])

vp1=Node(["vp1",2,102,])
vp2=Node(["vp2",3,103,])

vp1.reportee =[d1,d2]
vp2.reportee=[d5,d6,d7,d8]

#vp1=Node(["vp1",2,102,["d1","d2","d4"]])
#vp2=Node(["vp2",3,103,["d5","d6","d7","d8"]])

vp3= Node(["vp3",4,104,[]])

root.reportee=[vp1,vp2,vp3]


tries = Tree()
print(tries.findSeatNo_data("d1"))




print(root.reportee, root.reportee, type(root.reportee))
print(vp2.reportee, vp2.name_Data, type(vp2.reportee))
for item in vp2.reportee:
    print(item, type(item))

