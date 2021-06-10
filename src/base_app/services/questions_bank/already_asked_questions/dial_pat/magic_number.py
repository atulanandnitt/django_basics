import copy


# number_copy = copy.deepcopy(number)
def valid_input(number, n):
    if len(number) < n:
        return False


def lucky_number(number, n):
    if not valid_input(number, n):
        return False





if __name__ == '__main__':
    number = [1, 2, 3, 4, 5, 4, 3, 8, 2, 9, 9, 9]
    lucky_number(number, 7)

