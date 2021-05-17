#https://practice.geeksforgeeks.org/problems/find-the-fine/0

def maxFine(date,carNo,fineAmount):
    evenDayFine=0
    oddDayFine=0
    maxFine=0
    if type(fineAmount) == list:
        for car1,fine1, in zip(carNo,fineAmount):
            if date %2 ==0 and car1 %2 == 1:
                evenDayFine += fine1
            elif date %2 ==1 and car1 %2 == 0:
                oddDayFine += fine1
        
        maxFine = max(evenDayFine ,oddDayFine)
    else:
        if date %2 ==0 and carNo %2 == 1:
                evenDayFine += fineAmount
        elif date %2 ==1 and carNo %2 == 0:
                oddDayFine += fineAmount
        maxFine = max(evenDayFine ,oddDayFine)
    return maxFine

t=1#int(input())

for _ in range(t):
    N,date=1,9#map(int,input().strip().split())
    carNo=9258#list(map(int , input().strip().split()))
    fineAmount=1000#list(map(int , input().strip().split()))
    
    print(maxFine(date,carNo,fineAmount))


print(-18%-7)