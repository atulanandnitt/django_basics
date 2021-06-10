# code
def num_of_water(k, line, index):
    if index > line:
        return 0

    last_line = [0] * line
    last_line[0] = k

    for i in range(1, line):
        curr_line = [0] * line
        curr_line[0] = max(0, (last_line[0] - 1) / 2)

        for j in range(1, i + 1):
            curr_line[j] = max(0, (last_line[j - 1] - 1) / 2) + max(0, (last_line[j] - 1) / 2)

        last_line = curr_line

    ans = min(1, last_line[index - 1])
    ans = int(ans * 1000000)
    ans = ans / 1000000
    return ans


t = int(input())
for _ in range(t):
    k = int(input())
    line = int(input())
    index = int(input())
    print(num_of_water(k, line, index))
