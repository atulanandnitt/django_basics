

def subStringfun(str):
    subString=[]
    print("str :", str)
    length = len(str)
    i,j=0,0
    while i<length:
        j=i
        while j<length:
            subString.append(str[i:j+1])
            j+=1
        i+=1
    return subString
"""
subString1=[]
str="atulAnand"
length = len(str)
i,j=0,0
while i<length:
    j=i
    while j<length:
        subString1.append(str[i:j+1])
print(subString1)   
"""
print(subStringfun("atul"))

def word_split(inputStr,listStr):
    subString=subStringfun(inputStr)
    sol=[]
    for item in listStr:
        if item in subString:
            sol.append(item)
    return sol

print(word_split('themanran',['the','man','ran']))
print(word_split('ilovedogsJohn',['i','am','a','dogs','lover','love','John']))