import copy


def get_num_left_most_pos(number, num):
    """
    :param number:
    :return:
    """
    # O(n)
    pos = len(number) -1
    for item in number:
        print(number[pos])
        if number[pos] == num:
            return pos
        pos = pos -1

    return pos


def big_number():
    """

    :return:
    """
    # number = [9,8,5,6,9,4,9]
    number = [9, 8, 7, 6, 5, 4]
    # O(nlogn) sorting
    sorted_number = copy.deepcopy(number)
    sorted_number.sort(reverse=True)
    print(number, sorted_number)

    idx = 0
    for sorted, item in zip(sorted_number, number):

        if sorted == item:
            idx += 1
            continue
        else:
            pos = get_num_left_most_pos(number, sorted)
            print(pos, sorted, number)
            temp = number[idx]
            number[idx] = number[pos]
            number[pos] = temp
            break


    # Overall O(nlogn)
    print('Result:', number)

big_number()