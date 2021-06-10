# code

def merge_two_sorted_arrays(list1, list2):
    l1, l2 = len(list1), len(list2)
    i1, i2 = 0, 0
    # while i1 < (l1 - 1) and i2 < (l2 - 1):
    while i1 < (l1) and i2 < (l2):
        if list1[i1] < list2[i2]:
            i2 += 1
            continue
        if list1[i1] > list2[i2]:
            temp = list1[i1]
            list1[i1] = list2.pop(i2)
            for idx in range(len(list2)):
                if list2[idx] > temp:
                    list2.insert(idx, temp)
                    break
            i1 += 1
        print(list1)
        print(list2)
    return list1, list2
    # while i1 < (l1-1):


t = 1
# int(input())
for _ in range(t):
    # waste = int(input())
    # n, m = map(int, input().strip().split())
    list1 = [1, 3, 5, 7] #list(map(int, input().strip().split()))
    list2 = [0, 2, 6, 8, 9]#list(map(int, input().strip().split()))
    ans1, ans2 = merge_two_sorted_arrays(list1, list2)
    print(ans1 + ans2)
    # print(ans2)