

def chkPalindrom(str1):
    flag =False
    for i in range(len(str1)):
        print("str1[i] :", str1[i] , "str1[len(str1) -1 - i] : " ,str1[len(str1) -1 - i])
        if str1[i] == str1[len(str1) -1 - i]:
            continue
        else:
            flag =False
            return flag
    flag = True
    return flag

    """
    flag=False
    
    d1=dict([(key,str1.count(key)) for key in set(str1)])
    d2=dict([(key,str1.count(key)) for key in set(str1)])
    
    d3 = set(d1) & set(d2)
    print(d3)
    
    for i in range(len(d3)):
      if d1[i] == d2[i]:
          continue
      else:
          flag =False
          return flag
    return flag
    """
#str1="atul anand"
str1="DALAD"
if chkPalindrom(str1):
    print("its palindrom")
else:
    print("its NOT palindrom")
        
        


def commonElements(str1,str2):
    list1=[]
    list2=[]
    for item in str1:
        list1.append(item)
    for item in str2:
        list2.append(item)
    
    dict1=dict([(key,list1.count(key)) for key in set(list1)])
    dict2=dict([(key,list2.count(key)) for key in set(list2)])
    
    dict3= set(dict1) & set(dict2)
    dict4=dict()
    for key in dict3:
        dict4[key]=min(dict1[key],dict2[key])
    
    print(dict4)
    
    #values for str1 to be removed
    removeFromStr1=[]
    for key in dict1:
        try:
            removeFromStr1.append([key,dict1[key] - dict4[key]])
        except:
            removeFromStr1.append([key,dict1[key]])

    #values for str1 to be removed
    removeFromStr2=[]
    for key in dict2:
        try:
            removeFromStr2.append([key,dict2[key] - dict4[key]])
        except:
            removeFromStr2.append([key,dict2[key]])

    removeFromStr1.sort(key =lambda y:y[0])
    removeFromStr2.sort(key =lambda y:y[0])      #[' ', 1]       means removing a space
    return removeFromStr1,removeFromStr2
    
    
removeFromStr1,removeFromStr2=commonElements("atul","atul anand")    
print("removeFromStr1 :",removeFromStr1,"removeFromStr2 ",removeFromStr2)


            