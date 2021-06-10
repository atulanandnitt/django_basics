
def min_jump(pos, obstacles):
    if len(obstacles) == 0:
        return 0

    obst = obstacles.pop(0)

    if obst == pos:
        if obst == 1:
            return min(min_jump(2, obstacles)+1, min_jump(3, obstacles) + 1)
        elif obst == 2:
            return min(min_jump(1, obstacles) + 1, min_jump(3, obstacles) + 1)
        elif obst == 3:
            return min(min_jump(1, obstacles) + 1, min_jump(2, obstacles) + 1)
    else:
        return min_jump(pos, obstacles)


if __name__ == '__main__':
    # print(min_jump(3, [2,1,2])) # Car game wala Q5
    # print(min_jump(2, [2, 1, 2]))  # Car game wala Q5
    print(min_jump(2, [2,3,2, 1,3, 1]))  # Car game wala Q5
    print(min_jump(2, [3,2,2,1,2,1]))
    print(min_jump(2, [2,1,3,2,3,1,1,3]))
