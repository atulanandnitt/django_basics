#code


def revUnique(str1):
    set1= set()
    stack1=[]
    revStr=""
    for item in str1:
        stack1.append(item)
        
    
    while 1:
            
        try:
            char1= stack1.pop()
            
            if char1 in set1 or char1==" ":
                continue
            else:
                revStr += char1
                set1.add(char1)

        except:
            break
        
    return revStr

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
            
        str1 = input()
        print(revUnique(str1))