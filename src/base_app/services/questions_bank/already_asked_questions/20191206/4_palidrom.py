def create_pal(dict1,only_req):
    list1 = list()
    if len(only_req) % 2 == 0:
        for key1,val1 in dict1.items():
            for i in range(val1 / 2):
                list1.append(key1)
                list1.insert(0,key1)
    else:
        for key1,val1 in dict1.items():
            if val1 %2 ==0:
                for i in range(val1 / 2):
                    list1.append(key1)
                    list1.insert(0,key1)
            if val1 %2 ==1:
                list1.insert(len(list1) / 2, key1)
                val1 -= 1
                for i in range(val1 / 2):
                    list1.append(key1)
                    list1.insert(0,key1)
    return list1


def is_palindrom(dict1,only_req):
    if len(only_req) % 2 == 0:
        for key1,val1 in dict1.items():
            if val1 % 2 == 1:
                return 0
        pal = create_pal(dict1,only_req)
        return pal
    else:
        counter = 0
        for key1,val1 in dict1.items():
            if val1 % 2 == 1:
                counter += 1

        if counter == 1:
            pal = create_pal(dict1,only_req)
            return pal
        else:
            return 0


def find_palindrom(only_req):
    dict1 = {key:only_req.count(key) for key in set(only_req)}
    pal = is_palindrom(dict1,only_req)
    if pal:
        return pal
    else:
        return -1


def palindrom(str):
    if str[0] == '-':
        str = str[1:]
    only_req = list()
    for chr1 in str:
        if ( (ord(chr1) >= 48 and ord(chr1) <= 57) or (ord(chr1) == 45) ):
            only_req.append(chr1)
    sol = find_palindrom(only_req)
    return sol

# sol = palindrom("-co?3d-5er45,-3")
sol = palindrom("-co?3d-5er444445,-3")
# sol = palindrom("-g4e3e5k3s4")

# sol = palindrom("-nu23m-2")

if sol == -1:
    print("-1")
else:
    solStr = ""
    for item in sol:
        solStr += str(item)
    print(solStr)
