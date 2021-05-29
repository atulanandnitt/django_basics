
def removeDuplicates(str1):
    for i in range(len(str1)):
        for j in range(i+1,len(str1)):
            if (str1[i] == str1[j]):
                if (j == len(str1)):
                    str1 = str1[:i] + str1[i+1:j]
                else:
                    str1 = str1[:i] + str1[i+1:j] + str1[j+1:]




    print(str1)
removeDuplicates("atulanand")





def isContainsAllAlphabet(str1):
    dict1= {key:str1.count(key) for key in set(str1)}
    print(dict1)
    allKeys = dict1.keys()
    for i in range(26):
        if chr(ord('a')+i) not in allKeys:
            return False
    else:
        return True
            
            
    
print(isContainsAllAlphabet("atulanand"))
str1=""
for i in range(26):
    str1 += chr(ord('a')+i)
    
print(isContainsAllAlphabet(str1))


def removeDuplicates2(str1):
    dict1= {key:str1.count(key) for key in set(str1)}
    print(dict1)
    solStr=""
    for key1,val1 in dict1.items():
        if val1 %2 ==1:
            solStr += key1
                    
    print(solStr)
    
removeDuplicates2("atulanand")




def seperateZeroAndOnes(str1):
    zeros=""
    ones=""
    for i in range(len(str1)):
        if str1[i] == "0":
            zeros += str1[i]
        else:
            ones += str1[i]
            
    print(ones)
    print(zeros)


def seperateZeroAndOnes2(str1):
    zeros=0
    ones=0
    countZeros = str1.count("0")
    countOnes = str1.count("1")
    zeros=[0 for i in range(countZeros)]
    ones=[1 for i in range(countOnes)]
    print(str(zeros))
    print(str(ones))
    
    
seperateZeroAndOnes("00010111010101011101")
seperateZeroAndOnes2("00010111010101011101")

























def removeSpecialChar(str1):
    setOfAlphaNumeric = set()
    specialCharFound=""
    alhaNumericChar=""
    for i in range(26):
        setOfAlphaNumeric.add(ord('a')+i)
    for i in range(26):
        setOfAlphaNumeric.add(ord('A')+i)
        
    for i in range(10):
        setOfAlphaNumeric.add(ord('0')+i)
        
    for i in range(len(str1)):
        if ord(str1[i]) in setOfAlphaNumeric:
            alhaNumericChar += str1[i]
        else:
            specialCharFound += str1[i]

    print(specialCharFound)
    print(alhaNumericChar)         
    
    
    
removeSpecialChar("sdafasdgarqet6245treghfer@#$@$^^%&fhwrt345%$")    
                  
                  
                  