#https://practice.geeksforgeeks.org/problems/find-k-th-character-in-string/0/?ref=self

def binaryFun(m):
    val=""
    while m >1:
        val += str(m % 2)
        #print("val is :",val)
        #print("m is ",m)
        m=m // 2
    val += str(m % 2)
    return val

    
def sol(m,k,n):
    bin_m= binaryFun(m)
    str1=bin(m)
    bin_m=str1[2:]
    print(bin_m)
    #m=11
    print("binary val is :",bin(m)[2:])
    print("decimal val is ",int(bin(m),2))
    #print("decimal val is ",'1111'.fromBinaryToInt())
    #new_bin_m=""
    temp=""
    for _ in range(n):
        for item in bin_m:
            if item == '1':
                temp +='10'
            elif item =='0':
                temp +='01'
        bin_m = temp
        temp=""
        #print(bin_m)
    return bin_m[k]
        
print(" {} is mt name","atul")
print("%s %s is my full name" %("Atul"," Anand"))

t=1#int(input())
for _ in range(t):
    m,k,n=42,47,8#map(int,input().strip().split())
    #m,k,n=32,17,9#map(int,input().strip().split())
    #m,k,n=11,6,4#map(int,input().strip().split())
    print("sol is ",sol(m,k,n))
