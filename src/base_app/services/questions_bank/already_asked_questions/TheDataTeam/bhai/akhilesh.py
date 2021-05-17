import re

def match_regex():
    """

    :return:
    """

    print(re.compile(r'''
        ^
        [^a]*
        (
            (
                a[^a]*
            ){2}
        # if there must be at least 2 (not just 0), change the
        # '*' on the following line to '+'
        )*
        $
        ''',re.IGNORECASE|re.VERBOSE)
          )


def match_matrix(node, relation, weight_list):
    """

    :return:
    """

    node_pair_list = dict()

    if node is None:
        return

    for weight in weight_list:
        node_1 = weight[0]
        node_2 = weight[1]
        node_pair = '{}-{}'.format(min(node_1, node_2), max(node_1, node_2))

        if node_pair_list.get(node_pair) is None:
            node_pair_list[node_pair] = list()
        node_pair_list[node_pair].append(weight[2])

    print(node_pair_list)
    max_len = 0
    max_value = 0
    for key, value in node_pair_list.items():

        print(key, value)
        length = len(value)

        if length >= max_len:
            max_len = length
            value = int(key.split('-')[0]) * int(key.split('-')[1])

            if value >= max_value:
                max_value = value
    print(max_value)
    return max_value


def min_jump(pos, obstacles):
    """

    :param pos:
    :param obstacles:
    :return:
    """

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


def rotate(arr):
    """

    :param arr:
    :return:
    """
    first = arr[0]

    for i in range(0, len(arr)-1):
        arr[i] = arr[i+1]
    arr[len(arr)-1] = first


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


def rotate_number(work_arr, rotate_arr):
    """

    :param work_arr:
    :param rotate_arr:
    :return:
    """
    output_list = list()

    for i in range(0, len(rotate_arr)):
        output_list.append(0)

    dict_list = list()
    idx = 0
    for item in rotate_arr:
        dict_list.append(dict(
            value=item,
            index=idx
        ))
        idx += 1

    dict_list = sorted(dict_list, key=lambda i: i['value'])

    rotate_count = 0
    print(dict_list)
    for item in dict_list:
        print(item['value']-rotate_count)
        for i in range(0, item['value']-rotate_count):
            rotate(work_arr)
            rotate_count += item['value']-rotate_count
            output_list[item['index']] = get_max_idx(work_arr)

    print(output_list)


def election(candidates):
    """

    :param candidates:
    :return:
    """
    voting = set()
    votes = dict()

    for name in candidates:
        if votes.get(name) is None:
            votes[name] = 1
        else:
            votes[name] += 1

    max_vote = 0
    winner = None
    for key, value in votes.items():
        if value >= max_vote:
            max_vote = value
            if winner is None or key > winner:
                winner = key

    print(votes)
    print(winner, max_vote)


def mark_visit(arr_dict, start, end, size):
    """

    :param arr:
    :param start:
    :param end:
    :return:
    """
    print(start, end, size)

    while True:
        if arr_dict.get(start) is None:
            arr_dict[start] = 1
        else:
            arr_dict[start] += 1

        if start == end:
            break

        if start == size:
            start = 1
            continue

        start += 1


def visit_nodes(arr, paths):
    """

    :return:
    """
    arr_dict = dict()

    for i in range(0, len(paths) -1):
        mark_visit(arr_dict, paths[i], paths[i+1], len(arr))

    print(arr_dict)


if __name__ == '__main__':
    #  Q2 and Q4 are pending
    match_regex() # This not working
    tuple_list = [(1,2,2),(1,2,3),(2,3,1),(2,3,3),(2,4,4)] # Graph wala Q6
    match_matrix(4,5,tuple_list)
    print(min_jump(3, [2,1,2])) # Car game wala Q5

    print(rotate_number([1,2,3],[1,2,3,4])) # Array rotation wala Q3
    election(['Alex', 'Michael', 'Harry', 'Dave', 'Michael', 'Victor', 'Harry', 'Alex', 'Mary', 'Mary']) #Q1
    visit_nodes([1,2,3], [1,3,2,3])
