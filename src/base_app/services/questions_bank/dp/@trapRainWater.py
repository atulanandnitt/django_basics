# https://practice.geeksforgeeks.org/problems/trapping-rain-water/0

def trapping_rain_water2(list1):
    # print(list1)
    l_2_r = [0 for _ in list1]
    r_2_l = [0 for _ in list1]
    l_max = list1[0]
    r_max = list1[-1]
    l_2_r[0]= list1[0]
    r_2_l[-1]=list1[-1]

    for i in range(1, len(list1)):
        l_2_r[i] = max(l_max, list1[i])
        l_max = max(l_max, list1[i])

    for i in range(len(list1)-2, -1, -1):
        r_2_l[i] = max(r_max, list1[i])
        r_max = max(r_max, list1[i])

    # print(l_2_r)
    # print(r_2_l)

    water = 0
    for i in range(1,len(list1)-1):
        water += min(l_2_r[i], r_2_l[i]) - list1[i]

    return water

T = 1#int(input())

for _ in range(T):
    waste = 4#int(input())
    list1 = [7,4,0,9]#map(int, input().strip().split(" "))
    print(trapping_rain_water2(list1))



def trapRainWater(list1):
    left=[0 for _ in range(len(list1))]
    left[0]=list1[0]
    right=[0 for _ in range(len(list1))]
    right[-1]=list1[-1]
    
    for i in range(1,len(list1)):
        left[i]=max(left[i-1],list1[i])
    
    for j in range(len(list1)-2,-1,-1):
        right[j]=max(right[j+1],list1[j])

    water=0        
    for k in range(len(list1)):
        if min(left[k],right[k]) >0:
            water += min(left[k],right[k]) - list1[k]
    print(water)
    return water


list1=[5,7,2, 0, 2,7,5]
print("sol : ",trapRainWater(list1))
        
