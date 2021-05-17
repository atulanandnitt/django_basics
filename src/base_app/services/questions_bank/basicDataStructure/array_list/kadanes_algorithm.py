# code

def implement_kadanes_algorithm(list1):
    sum_till_now = 0
    max_sum = 0
    for item in list1:
        if sum_till_now >= 0:
            sum_till_now += int(item)
            max_sum = max(max_sum, sum_till_now)
        if sum_till_now < 0:
            max_sum = max(max_sum, sum_till_now)
            sum_till_now = 0
        # print(item, sum_till_now, max_sum)
    if max(list1) < 0:
        return min(list1)
    return max_sum


t = 1
# int(input())
for _ in range(t):
    # waste = int(input())
    list1 = [-2, 5, -1]
    # list(map(int, input().strip().split()))
    ans = implement_kadanes_algorithm(list1)
    print(ans)