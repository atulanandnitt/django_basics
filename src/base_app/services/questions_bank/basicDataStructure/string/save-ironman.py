#https://practice.geeksforgeeks.org/problems/save-ironman/0


t = 1#int(input())

for i in range(t):
    inputStrOriginal="Ab1?/1Ba"#input()
    inputStr=""
    for item in inputStrOriginal:
        if ((ord(item) >= 65 and ord(item) <= 65+25) ):
            inputStr += item
        if (ord(item) >= 97 and ord(item) <= 97+25):
            inputStr += chr(ord(item) - (97-65))
        if  (ord(item) > 47 and ord(item) <= 57):
            inputStr += item
        
    #print("inputStr ",inputStr)    
    revStr=""
    l=len(inputStr)
    for j in range(len(inputStr)):
        revStr += inputStr[l -1 -j]
    print("revStr",revStr)
    if revStr == inputStr:
        print("YES")
    else:
        print("NO")   
        
"""

for _ in range(int(input())):
    s = input()
    s = s.lower()
    n = len(s)
    res = ""
    
    for i in range(n):
        val = ord(s[i])
        if (val > 47 and val <= 57) or (val >= 97 and val < 123):
            res += s[i]
            
    if res == "".join(reversed(res)):
        print("YES")
    else:
        print("NO")

"""        