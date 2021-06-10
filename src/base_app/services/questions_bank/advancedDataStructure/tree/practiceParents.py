#parent practice

class Node:
    def __init__(self,valList):
        self.empId=valList[0]
        self.locId=valList[1]
        self.reportee=None#valList[2]
        
def findlocId(empIdVal):
    pass
    
    
    
    
    
svp=Node([1,101])    
vp1=Node([2,102])
vp2=Node([3,103])
vp3=Node([4,104])
svp.reportee=[vp1,vp2,vp3]

print(svp.reportee)