import copy


def is_valid_2_digit(a, b):
    """

    :param a:
    :param b:
    :return:
    """

    str = '{}{}'.format(a, b)
    if int(str) < 59:
        return True
    else:
        return False


def is_lucky_number(number, num):
    """
    To find out a numbers as lucky means grouping
    the number in 7 parts and none if the part should be more than 59
    Ex: [1,2,3,4,5, 4,3,8, 2, 9, 9, 9]
    => 12, 34, 54, 38, 29, 9, 9 is lucky
    However
     Ex: [1,2,3,4,5, 4,3,8, 9, 9, 9, 9]
     12, 34, 54, 38, 99, 9, 9 is not lucky
     also if partition like
     12, 34, 54, 38, 9, 9, 9, 9 then it would be 8 partition we
     need to do only  7 partition
    :param number:
    :return:
    """
    # Base condition
    print("number is : {0} and num is :{1}".format(number, num))
    if len(number) <= 2:
        if num > len(number):
            return False
        elif num == len(number):
            print('Result', num, number)
            return True
        elif num <= 0:
            return False
        else:

            if is_valid_2_digit(number[0], number[1]):
                return True
            else:
                return False
    else:
        # print(num, number)
        number_copy = copy.deepcopy(number)
        number_copy.pop(0)
        first = is_lucky_number(number_copy, num-1)
        # print("first : {0}".format(first))
        a = number.pop(0)
        b = number.pop(0)
        # print("number : {0} and number_copy : {1}".format(number, number_copy))
        second = is_lucky_number(number, num-1) and is_valid_2_digit(a, b)

        return first or second


def lucky_number():
    """
    Determine if a number givens in the list is lucky numbers
    :param number:
    :return:
    """
    # 59, 1 or 2
    number = [1, 2, 3, 4, 5, 4, 3, 8, 2, 9, 9, 9]

    # if is_lucky_number(number, 7) is True:
    print("calling is_lucky_number : ")
    if is_lucky_number(number, 7):
        print("This is lucky")
    else:
        print("This is not lucky")


if __name__ == '__main__':
    lucky_number()
