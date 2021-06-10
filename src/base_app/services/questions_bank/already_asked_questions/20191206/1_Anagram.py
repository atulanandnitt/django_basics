def read_file(fileName):
    data = ""
    with open(fileName, "r") as f1:
        data = f1.read()
    return data

fileName = "Sample1.txt"
data = read_file(fileName)

data_list = data.split(" ")
# sorted_data = sorted(data_list)


def data_cleaning(item1):
    clean_item1 = ""
    for chr1 in item1:
        if ( (ord(chr1) >= 65 and ord(chr1) <= 90)
            or (ord(chr1) >= 97 and ord(chr1) <= 122) ):
            clean_item1 += str(chr1)
    return clean_item1


def is_anagram(item1, item2):
    item1 = item1.lower()
    item2 = item2.lower()
    item1 = data_cleaning(item1)
    item2 = data_cleaning(item2)
    if len(item1) != len(item2) or item1 == item2:
        return False

    dict1 = {key1:item1.count(key1) for key1 in set(item1)}
    dict2 = {key1: item1.count(key1) for key1 in set(item2)}

    if len(dict1) == len(dict2):
        for key1, val1 in dict1.items():
            if key1 in dict2.keys():
                if str(dict2[key1]) != str(dict1[key1]):
                    return False
            else:
                return False
        return True
    else:
        return False


def both_elements_are_new(item1, item2,anagram_list):
    for item in anagram_list:
        if item1 in item or item2 in item:
            return False
    return True


anagram_list = list()
for i in range(len(data_list)):
    for j in range(i+1,(len(data_list))):
        item1 = data_cleaning(data_list[i])
        item2 = data_cleaning(data_list[j])
        if is_anagram(item1, item2):
            temp = [item1, item2]
            temp.sort()
            if both_elements_are_new(item1, item2,anagram_list):
                anagram_list.append(temp)
            else:
                for i in range(len(anagram_list)):
                    if ( (item1 in anagram_list[i][0] or item1 in anagram_list[i][1])
                        and (item2 not in anagram_list[i][0] or item2 not in anagram_list[i][1]) ):
                        anagram_list[i].append(item2)
                    elif ( (item1 not in anagram_list[i][0] or item1 not in anagram_list[i][1])
                        and (item2 in anagram_list[i][0] or item2 in anagram_list[i][1]) ):
                        anagram_list[i].append(item1)


anagram_list.sort(key=lambda x:x[0])
print(anagram_list)
