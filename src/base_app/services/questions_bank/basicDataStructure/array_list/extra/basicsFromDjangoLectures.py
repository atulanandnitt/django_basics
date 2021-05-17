def findSeq123(list1):
    for i in range(len(list1)):
        if list1[i] == 1:
            if list1[i+1] ==2 and list1[i+2] ==3:
                return True
    else:
        return False
        


list1 =[1,1,1,2,4,5,6,7,1,3]
print(findSeq123(list1))


str1="Heeololeo"
for i in range(len(str1)):
    if i%2 ==0:
        print(str1[i], end="")



def findSubStr(str1,str2):
        
    if str4 in str5:
        return True
        
    if str5 in str4:
        return True
    
    else:
        return False


str2="Hiabc"
str3="ABC"

str4=str2.lower()
str5=str3.lower()
print(str4,str5)

print(findSubStr(str4,str5))




def doubleChar(str1):
    str2=""
    for i in range(len(str1)):
        str2 += str1[i]
        str2 += str1[i]
    return str2


str1="Heeololeo"        
print(doubleChar(str1))        
    


def simpleGame(given,guess):
    if given == guess:
        return "Match"
    
    gi=list()
    while given >9:
        gi.append(given%10)
        given = given // 10
    gi.append(given)
        
    gu=list()
    while guess >9:
        gu.append(guess%10)
        guess = guess // 10
    gu.append(guess)
    
    gi.sort()
    gu.sort()
    print(gi,gu)
    if gi ==gu:
        return "Close"
    
    else:
        return "Nope"    
    
given=123
guess=321
    

print(simpleGame(given,guess))    