#https://practice.geeksforgeeks.org/problems/string-comparison/0


def stringComparison(str1,str2):
    for i in range(min(len(str1),len(str2))):
        if ord(str1[i]) > ord(str1[i]):
            return 1
        elif ord(str1[i]) > ord(str1[i]):
            return -1
    if len(str1) < len(str2):
        return -1
    elif len(str2) < len(str1):
        return 1
    else:
        return 0

str1="Atul Anand"
str2="Atul Anan"

print(stringComparison(str1,str2))