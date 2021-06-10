# def chocolate_distribution_problem(list1, std):
#     list2 = sorted(list1)
#     print(list2)
#     gap = list()
#     packet_selected = list()
#     for i in range(len(list2) - 1):
#         gap.append(list2[i + 1] - list2[i])
#     print("gap is : {0}".format(gap))
#     selected_index = set()
#     inf = 999999
#     for _ in range(std):
#         minpos = gap.index(min(gap))
#         gap[minpos] = inf
#         print("minpos : {0}".format(minpos), end="")
#         if len(packet_selected) < std and minpos not in selected_index:
#             packet_selected.append(list2[minpos])
#             selected_index.add(minpos)
#         if len(packet_selected) < std and minpos+1 not in selected_index:
#             packet_selected.append(list2[minpos + 1])
#             selected_index.add(minpos+1)
#         # if len(packet_selected) == std:
#         #     break
#
#         print("packet_selected till now : {0}".format(packet_selected) , end= "")
#         print("selected_index till now : {0}".format(selected_index))
#     return max(packet_selected) - min(packet_selected)


def chocolate_distribution_problem_2(list1,k):
    minGap=max(list1) - min(list1)#infinity
    list1.sort()
    for i in range(len(list1)- k+1):
        print(list1[i:i+k])
        tempGap= max(list1[i:i+k]) - min(list1[i:i+k])
        minGap=min(tempGap,minGap)
    return minGap
t = 1
# int(input())

for _ in range(t):
    # waste = int(input())
    list1 = [7, 3, 2, 4, 9, 12, 56]
    std = 3
    # list1 = [87,78,16,94,36,87,93,50,22,63,28,91,60,64,27,41,27,73,37,12,69,68,30,83,31,63,24,68,36,30,3,23,59,70,68,94,57,12,43,30,74,22,20,85,38,99,25,16,71,14,27,92,81,57,74,63,71,97,82,6,26,85,28,37,6,47,30,14,58,25,96,83,46,15,68,35,65,44,51,88,9,77,79,89]
        # list(map(int, input().strip().split()))
    # std = 61
    # int(input())
    # ans = chocolate_distribution_problem(list1, std)
    ans = chocolate_distribution_problem_2(list1, std)
    print(ans)

# gap = [1, 1, 3, 2, 3, 44]
# print(gap)
# minpos = gap.index(min(gap))
# gap.pop(minpos)
# print(gap)

