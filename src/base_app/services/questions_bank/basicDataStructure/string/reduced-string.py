#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the super_reduced_string function below.
def super_reduced_string(s):
    s2=""
    for i in range(len(s) -1):
        if s[i] == s[i+1]:
            i += 2
            print(i)
            continue
        else:
            s2 += s[i]
            print(s2, i)
    return s2      

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = "aaabccddd"#input()

    result = super_reduced_string(s)

    print(result)
