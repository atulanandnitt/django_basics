def is_anagram(str1,str2):
    dict1 = {key:str1.count(key) for key in set(str1)}
    dict2 = {key: str2.count(key) for key in set(str2)}

    if dict1.keys() == dict2.keys():
        for key,val in dict1.items():
            if dict1[key] == dict2[key]:
                continue
            else:
                return False
        return True
    else:
        return False


print(is_anagram("str1","trs"))
