
def knapsack(values,weights,totalWt):
    T=[]
    for i in range(len(weights)+1):
        row=[]
        for j in range(totalWt):
            row.append(0)
        T.append(row)
    print(T)
    
    for i in range(len(weights)):
        for j in range(totalWt):
            if j ==0:
                T[i][j]=0
            else:
                T[i][j] = max(T[i-1][j],val)
            
    



values=[2,2,4,5]
weights=[2,4,6,9]
totalWt=8

print(knapsack(values,weights,totalWt))    