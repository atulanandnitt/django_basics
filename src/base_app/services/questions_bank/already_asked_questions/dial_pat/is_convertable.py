import copy
import enchant

# http://www.blazedemo.com:8080/github-webhook/
def is_valid_input(src_word, dest_word, eng_dict1):
    if eng_dict1.check(src_word) and eng_dict1.check(dest_word) and (len(src_word) == len(dest_word)):
        return True
    else:
        return False


def is_word_connected(src_word, dest_word, eng_dict1, set1):
    """
    :param src_word:
    :param dest_word:
    :return:
    """

    if src_word == dest_word:
        print(src_word, dest_word, "This is good")
        return True

    if "".join(dest_word) in set1:
        print("This is also good")
        return True

    for idx in range(0, len(src_word)):
        src_word_prev = copy.deepcopy(src_word)

        # Prev eng_dictionary word based on idx position
        if ord(src_word_prev[idx]) == 97:
            print("src_word_prev[idx] : {0}".format(src_word_prev[idx]))
            src_word_prev[idx] = chr(122)
        else:
            src_word_prev[idx] = chr(ord(src_word_prev[idx])-1)
            
        if "".join(src_word_prev) not in set1:
            set1.add("".join(src_word_prev))
            if eng_dict1.check("".join(src_word_prev)) is True:
                if is_word_connected(src_word_prev, dest_word, eng_dict1, set1) is True:
                    return True

        # Next eng_dictionary word based on idx postion
        src_word_next = copy.deepcopy(src_word)
        if ord(src_word_next[idx]) == 122:
            src_word_next[idx] = chr(97)
        else:
            src_word_next[idx] = chr(ord(src_word_next[idx]) + 1)

        if "".join(src_word_next) not in set1:
            set1.add("".join(src_word_next))
            if eng_dict1.check("".join(src_word_next)) is True:
                if is_word_connected(src_word_next, dest_word, eng_dict1, set1) is True:
                    return True


def is_convertible():
    """
    Determine if two given English word is reachable to each other
    :param number:
    :return:
    """
    src_word = "Pat".lower()
    dest_word = "oat".lower()
    # src_word = "Pat".lower()  # Pat -> Put -> cut
    # dest_word = "cut".lower()
    set1 = set()
    set1.add(src_word)

    if is_valid_input(src_word, dest_word, enchant.Dict("en_US")):
        if is_word_connected(list(src_word), list(dest_word), enchant.Dict("en_US"), set1) is True:
            print("Both the word is connected")
        else:
            print("Both the word is not connected")


if __name__ == '__main__':
    is_convertible()
