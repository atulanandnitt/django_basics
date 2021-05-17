# -*- coding: utf-8 -*-
"""
Created on Thu Oct 25 22:05:45 2018

@author: Atul Anand
"""

original = [[1, 2, 3,10],
            [4, 5, 6,11],
            [7, 8, 9,12]
            ]


def rotated(array_2d):
    list_of_tuples = zip(*array_2d[::1])
    print(list_of_tuples)
    for t in list_of_tuples:
        print(list(t))
    return [list(elem) for elem in list_of_tuples]
    # return map(list, list_of_tuples)

print(list(rotated(original)))

# [[7, 4, 1], [8, 5, 2], [9, 6, 3]]


original = [[1, 2, 3,10],
            [4, 5, 6,11],
            [7, 8, 9,12]
            ]


d = list(zip(original))

for item in d:
    print(item)
    
    
print("val of d : ",d)

print(list(zip(*original)))

print(list(zip(*original[::-1])))

for tupple1 in (list(zip(*original))):
    n = len(tupple1)
    for i in range(n):
        print(tupple1[n-1-i] , end =" ")
    print()