# code

def pairs_with_specific_difference(list1, max_gap):
    list1.sort()
    sol_temp_list = list()
    sol_list = list()
    for i in range(0, len(list1) - 1):
        if abs(list1[i + 1] - list1[i]) < max_gap:
            sol_temp_list.append([list1[i], list1[i + 1]])
    print("sol_temp_list : {0}".format(sol_temp_list))

    prev = sol_temp_list[0]
    for cur in sol_temp_list[1:]:
        print("prev : {0} and cur: {1}".format(prev, cur))
        if abs(cur[1] - prev[0]) < max_gap and cur[0] == prev[1]:
            prev = cur

        elif cur[0] == prev[1]:
            sol_list.append(prev)
            prev = cur
        print("sol_list : {0}".format(sol_list))
    sol_list.append(prev)
    sol = 0
    for item in sol_list:
        sol += item[0] + item[1]
    return sol


t = 1
# int(input())

for _ in range(t):
    # waste = int(input())
    list1 = [3, 5, 10, 15, 17, 12, 9]
    max_gap = 4
    print(pairs_with_specific_difference(list1, max_gap))