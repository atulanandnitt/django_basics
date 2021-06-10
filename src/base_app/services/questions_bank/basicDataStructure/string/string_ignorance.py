#https://practice.geeksforgeeks.org/problems/string-ignorance/0



def string_ignorance(str1):
    dict1=dict()
    solStr=""
    
    for ch in str1:
        chLower= ch.lower()
        if chLower not in dict1.keys():
            dict1[chLower]=0
            
        dict1[chLower] += 1
        
        if dict1[chLower] % 2 ==0:
            continue
        else:
            solStr += ch
    return (solStr)
    
t= 1#int(input())

for _ in range(t):
    str1="It is a long day dear."#input()
    print(string_ignorance(str1))
    
"""   

#code
for i in range(int(input())):
    s=dict()
    final=""
    for str1 in input():
        k=str1.lower()
        if k not in s:
            s[k]=0
        s[k]+=1
        if s[k]%2==0:
            continue
        else:
            final+=str1
    print(final)    

#code
 
def string_ignorance(str1):
    dict
    


t=int(input())

for _ in range(t):
    str1=input()
    print(string_ignorance(str1))
    
s
Input:
2
It is a long day dear.
Geeks for geeks
Output:
It sa longdy ear.
Geks fore
"""    