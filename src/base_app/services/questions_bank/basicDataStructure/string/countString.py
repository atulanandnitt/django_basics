def count_no_of_occurance_before_p(str1,i):
    str2 = str1[:i-1]
    chr = str1[i-1]
    counter = str2.count(chr)
    return counter


N = 9#int(input())
str1 = "abacsddaa"# input()
Q = 2#int(input())
for _ in range(Q):
    index = 3# int(input())
    print(count_no_of_occurance_before_p(str1,index))

print("done")