#https://practice.geeksforgeeks.org/problems/transform-the-array/0


def transform_the_array(list1):
    for i in range(len(list1)):
        for j in range(len(list1) -1):
            if list1[j] == list1[j+1]:
                list1[j] = 2 * list1[j]
                list1[j+1] =0
    print(list1)
    return list1


list1=[2,4,5,0,0,5,4,8,6,0,6,8]
print(transform_the_array(list1))
    