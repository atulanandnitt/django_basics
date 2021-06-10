list1 = [1, 2, 4]
print(*list1)
print(list)


# list2 = [1,2,3,5,7,3,9,3,9]   -->
# 123573939   -- >   923573931

str1 = "Created a parking lot with 6 slots\nAllocated slot number: 1\nAllocated slot number: 2\nAllocated sl...: 4\nSorry, parking lot is full\nKA-01-HH-1234, KA-01-HH-9999, KA-01-P-333\n1, 2, 4\n6\nNot found\n"
str2 = "Created a parking lot with 6 slots\nAllocated slot number: 1\nAllocated slot number: 2\nAllocated sl...: 4\nSorry, parking lot is full\nKA-01-HH-1234, KA-01-HH-9999, KA-01-P-333\n1, 2, 4\n6\nNot found\n"
if str1 == str2:
    print("matched")

import copy

def get_max_and_left_pos(number):
    """
    :param number:
    :return:
    """
    number.reverse()
    pos = len(number) -1
    print(number, pos)
    max = 0
    max_pos = 0
    for item in number:
        if max < int(item):
            print(item, pos)
            max_pos = pos
            max = int(item)
        pos = pos -1

    return max, max_pos


def big_number():
    """

    :return:
    """
    # number = [1,3,1,9,9,8]
    number = [9,8,7,6,5,4]
    temp_number = copy.deepcopy(number)
    print(number)
    # Swap number with biggest and right most
    # Get max number, idea is to put in left most
    # O(n)
    max, max_pos = get_max_and_left_pos(number)
    pos = 0
    print(max, max_pos, temp_number)

    # O(n)
    for item in temp_number:
        if int(item) == max:
            pos += 1
            continue

        print('Hi',item, pos, max_pos, temp_number)
        temp_number[pos] = temp_number[max_pos]
        temp_number[max_pos] = item
        break

    print('Result:',temp_number)


if __name__ == '__main__':
    big_number()