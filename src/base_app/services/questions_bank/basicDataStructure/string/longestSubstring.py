#longest substring

def longestSubstringWithoutRepeatation(str1):
    tempList=[]
    maxlen=0
    maxTillNow =0
    for i in range(len(str1)):
        for j in range(i,len(str1)):
            if str1[j] not in tempList:
                tempList.append(str1[j])
                maxTillNow += 1
            else:
                break
        print("maxTillNow :", maxTillNow)
        maxlen = max(maxlen,maxTillNow)
        maxTillNow=0
        tempList=[]
        
    return maxlen



str1="werfvbjisrgvbn"

print("len(str1)", len(str1))
print(longestSubstringWithoutRepeatation(str1))



print((set(str1)))
print(len(set(str1)))    