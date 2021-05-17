# def rotate(arr):
#     """
#
#     :param arr:
#     :return:
#     """
#     first = arr[0]
#
#     for i in range(0, len(arr)-1):
#         arr[i] = arr[i+1]
#     arr[len(arr)-1] = first
#     return arr

# def rotate_number(work_arr, rotate_arr):
#     """
#
#     :param work_arr:
#     :param rotate_arr:
#     :return:
#     """
#     output_list = list()
#
#     for i in range(0, len(rotate_arr)):
#         output_list.append(0)
#
#     dict_list = list()
#     idx = 0
#     for item in rotate_arr:
#         dict_list.append(dict(
#             value=item,
#             index=idx
#         ))
#         idx += 1
#
#     dict_list = sorted(dict_list, key=lambda i: i['value'])
#
#     rotate_count = 0
#     print(dict_list)
#     for item in dict_list:
#         print(item['value']-rotate_count)
#         for i in range(0, item['value']-rotate_count):
#             rotate(work_arr)
#             rotate_count += item['value']-rotate_count
#             output_list[item['index']] = get_max_idx(work_arr)
#
#     print(output_list)
import copy

def rotate(work_arr, item):
    temp_work_arr = copy.deepcopy(work_arr)
    for i in range(item):
        tmp = temp_work_arr[0]
        for j in range(len(temp_work_arr) - 1):
            temp_work_arr[j] = temp_work_arr[j+1]
        temp_work_arr[len(temp_work_arr)-1] = tmp

    return temp_work_arr


def get_max_idx(arr):
    """

    :param arr:
    :return:
    """
    max_value = 0
    max_idx = -1
    idx = 0

    for item in arr:
        if item >= max_value:
            max_value = item
            max_idx = idx
        idx += 1
    return max_idx



def rotate_number_2(work_arr, rotate_arr):

    output_list = list()

    for item in rotate_arr:
        print("before rotation : {0}".format(work_arr))
        arr = rotate(work_arr, item)
        print("after rotation : {0}".format(arr))
        output_list.append(get_max_idx(arr))

    print(output_list)


if __name__ == '__main__':
    # print(rotate_number([1,2,3],[1,2,3,4,1,5])) # Array rotation wala Q3
    print(rotate_number_2([1, 2, 3], [1, 2, 3, 4, 1, 5]))  # Array rotation wala Q3
