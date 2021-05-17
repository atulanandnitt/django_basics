# code


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


def trappingRainWater(a):
    n = len(a)
    lo, hi, leftmax, rightmax, total = 0, n - 1, 0, 0, 0
    # print("leftmax :",leftmax,"rightmax ",rightmax)
    while lo <= hi:
        if leftmax < rightmax:
            # print("leftmax :",leftmax,"rightmax ",rightmax)
            if a[lo] > leftmax:
                leftmax = a[lo]
            else:
                total += leftmax - a[lo]
                # print("1 :",total)
            lo += 1
        else:
            # print("from else :","leftmax :",leftmax,"rightmax ",rightmax)
            # print(total , rightmax ,a[hi],hi)
            if a[hi] > rightmax:
                rightmax = a[hi]
            else:
                total += rightmax - a[hi]
                # print("2 :",total)
            hi -= 1
    return total


t = int(input())

for _ in range(t):
    waste = int(input())
    list1 = list(map(int, input().strip().split()))
    print(trappingRainWater(list1))