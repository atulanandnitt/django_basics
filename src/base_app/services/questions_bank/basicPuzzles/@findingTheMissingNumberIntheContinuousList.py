
def findingTheMissingNumberIntheContinuousList(arr):
    firstNo=arr.pop(0)
    print(firstNo)
    lastNo=arr.pop()
    print(lastNo)
    correctSum,addedSum=0,0
    for item in range(firstNo,lastNo):
        #correctSum = int(((lastNo-firstNo) * (lastNo + firstNo) )/2)
        correctSum = int((lastNo **2 - firstNo **2)/2)
        
    for item in arr:
        addedSum +=item
    print("correctSum,addedSum",correctSum,addedSum)
    missingnum= correctSum-addedSum

    print(missingnum)
        
    
array =[-5,-4,-3,-2,-1,0,1,2,3,4,6]
    
findingTheMissingNumberIntheContinuousList(array)    