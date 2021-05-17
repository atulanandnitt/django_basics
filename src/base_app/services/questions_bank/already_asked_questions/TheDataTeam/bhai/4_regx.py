import re

# def match_regex():
#     """
#
#     :return:
#     """
#
#     re.compile(r'''
#         ^
#         [^a]*
#         (
#             (
#                 a[^a]*
#             ){2}
#         # if there must be at least 2 (not just 0), change the
#         # '*' on the following line to '+'
#         )*
#         $
#         ''',re.IGNORECASE|re.VERBOSE)


def match_regex(the_string):
    print(re.subn('a', '', the_string)[1])
    print(re.subn('b', '', the_string)[1])
    print(re.subn('c', '', the_string)[1])
    print(re.subn('d', '', the_string)[1])


if __name__ == '__main__':
    the_string = "aabbbccdd"
    match_regex(the_string) # This not working
