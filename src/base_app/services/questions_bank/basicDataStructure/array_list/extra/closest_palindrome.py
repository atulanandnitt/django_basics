

def findMin(n,a,b,c):
    # print(n-c,n-b,n-a,c,b,a)
    if abs(n-c) < abs(n-b) and abs(n-c) < abs(n-a):
        return c;
    elif abs(n-b) < abs(n-a):
        return b;
    else:
        return a;
    
def replaceVal(num,index,val):
    return num[:index]+val+num[index+1:]

def generatePalin(num):
    # print(num)
    mid = len(num)/2-1;
    index = len(num)-1;
    while index>mid:
        num = replaceVal(num,index,num[(len(num)-1)-index]);
        index = index-1;
    return num;
def closestPalin(num):
    if int(num)>9:
        l = len(num)
        # print(l/2)
        palnum2 = int(generatePalin(num))
        palnum1 = int(generatePalin(str(int(num)-pow(10,int(l/2)))))
        palnum3 = int(generatePalin(str(int(num)+pow(10,int(l/2)))))
        
        print(palnum1 , palnum2 , palnum3)
        return findMin(int(num),palnum1,palnum2,palnum3)
    else:
        return num
        
def main():
    t = 1#int(input())
    for i in range(t):
        num = 981#int(input())
        print(closestPalin(str(num)));
        # print(k);
if __name__ == "__main__":
    main();


"""

def closest_palindrome(str1):
    if len(str1) %2 ==0:
            
        mid = len(str1)//2
        left = str1[:mid]
        right= str1[mid:]
        newRight=""
        for i in range(len(left)):
            newRight = str(left[i]) + newRight

        return left+newRight
        
    else:
            
        mid = len(str1)//2
        left = str1[:mid+1]
        right= str1[mid+1:]
 
        newRight=""
        for i in range(len(left)-1):
            newRight = str(left[i]) + newRight
        return left+newRight
    
t=int(input())



for _ in range(t):
    str1=input()
    print(closest_palindrome(str1))
"""    