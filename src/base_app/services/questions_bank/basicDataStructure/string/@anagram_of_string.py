#Anagram_of_String

# https://leetcode.com/explore/challenge/card/may-leetcoding-challenge/536/week-3-may-15th-may-21st/3332/

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        # if len(s) < len(p):
        #     s, p = p, s
        p_d = {key: p.count(key) for key in set(p)}
        sol = list()
        for i, item in enumerate(s):
            temp_s = s[i:i+len(p)] 
            temp_s_d = {key: temp_s.count(key) for key in set(temp_s)}
            if temp_s_d == p_d:
                sol.append(i)
        return sol


# https://leetcode.com/explore/challenge/card/may-leetcoding-challenge/536/week-3-may-15th-may-21st/3333/
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # if len(s2) < len(s1):
        #     s1, s2 = s2, s1
        s1_d = {key: s1.count(key) for key in set(s1)}
        sol = list()
        for i, item in enumerate(s2):
            temp_s2 = s2[i:i+len(s1)] 
            temp_s2_d = {key: temp_s2.count(key) for key in set(temp_s2)}
            if temp_s2_d == s1_d:
                return True
        return False

        
def Anagram_of_String2(str1,str2):
    commonStr=""
    
    dic1={key: str1.count(key) for key in str1}
    dic2={key: str2.count(key) for key in str2}
    dic3=dict()
    for key1,value1 in dic1.items():
        print(key1)
        if dic2[key1]:
            dic3[key1] =min(dic1[key1] , dic2[key1])
            
    print(dic3)
    for key,val in dic3.items():
        for i in range(val):
            commonStr += key
        
    return commonStr

str1="aaabbc"
dict1={key : str1.count(key) for key in set(str1)}
print(dict1)
dict1['z']=11
print("dict1  :  ",dict1)
str2="aabbbccccdd"

print(Anagram_of_String2(str1,str2))


def Anagram_of_String(str1,str2):
    commonStr=""
    for i in range(len(str1)):
        for j in range(len(str2)):
            if str1[i] == str2[j]:
                commonStr += str(str1[i])
                
    return commonStr


str1="bcadeh"
dict1={key : str1.count(key) for key in set(str1)}
print(dict1)
str2="hea"

print(Anagram_of_String(str1,str2))

list1=[1,2,3,4]
list2=[2,3,4,5]

for item1,item2 in zip(list1,list2):
    print(item1+item2)
    
list3=[[3,5],
       [1,6],
       [56,87]]
list3.sort(key = lambda  y:y[0])
print(list3)
    

student={
        
        "name":"atul",
        "roll no":123,
        "height":"5ft 1 inch",
        "friends":["a","b","c","d","e"],
        "fast friends":{"p","q","r","s","t"}
        }

student["enemy"]="anand"
print(student)

student["friends"].append("srishti")
print(student)