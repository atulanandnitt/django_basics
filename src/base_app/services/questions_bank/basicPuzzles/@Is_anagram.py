
class Node:
    
    def __init__(self,val):
        self.data = val
        self.next = None



class LL:
    
    def __init__(self):
        self.head= None
        
    def createLL(self,val):
        
        if self.head == None:
            self.head = Node(val)
            
            return
        
        
        else:
            temp = self.head
             while True:
                 
                 if temp.next :
                     temp = temp.next
                     continue
                 
                else:
                    
                     

"""def findMax(list1):
    max1=max(list1[0:2])
    max2= min(list1[0:2])
    s1= min(list1[0:2])
    s2= max(list1[0:2])
    
    print(s1,s2,max1,max2)
    
    for item in list1:
       if  
    max1= max(list1)
"""    

#if anagram or not

def ifAnagram(str1,str2):
    
    str1 = str1.strip()
    str2 = str2.strip()
    
    
    str1=str1.replace(" ","").lower()
    str2=str2.replace(" ","").lower()
    
    list1_sorted=sorted(str1)
    list2_sorted=sorted(str2)
    
    if list1_sorted == list2_sorted:
        return True
    else:
        return False
    
    str1_sorted="".join(list1_sorted)
    str2_sorted="".join(list2_sorted)
    
    print(str1_sorted,type(str1_sorted))
    print(str2_sorted)
    
    if str1_sorted == str2_sorted:
        return True
    else:
        return False
"""    
def stepsToMakeAnagram(str1,str2):
    if ifAnagram(str1,str2):
"""    

input_str1="atul is a good boy"
input_str2="altuis a good boy"

print(ifAnagram("atul","anand"))
print(ifAnagram("atulanand","luta aannd"))
print(ifAnagram("atul is a good boy","altuis a goodboy"))



print("method 2:::::::::::::::::::::::::")



#anagram by dictionary

def isAnagramDic(inputstr1,inputstr2):
    inputstr1 = inputstr1.replace(" ","").lower()
    inputstr2 = inputstr2.replace(" ","").lower()
    """
    inputList1,inputList2=[],[]
    for item in inputstr1:
        inputList1.append(item)

    for item in inputstr2:
        inputList2.append(item)
    """    
    inputList1=sorted(inputstr1)
    inputList2=sorted(inputstr2)
    
    dict1 = dict([(key,inputList1.count(key)) for key in set(inputList1)])
    dict2 = dict([(key,inputList2.count(key)) for key in set(inputList2)])
    
    print("dict1",dict1)
    print("dict2",dict2)
    if dict1 == dict2:
        return True
    else:
        return False
    
inputstr1="my name IS atul"
inputstr2="Atul is My NAme"


inputstr1.lower()
inputstr2.lower()

if isAnagramDic(inputstr1,inputstr2):
    print("its Anagram")
else:
    print("Its not Anagram")