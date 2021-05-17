"""

https://practice.geeksforgeeks.org/problems/word-wrap/0



Given an array of size N, which denotes the number of characters in one word. The task is simple, count the number of words in a single line with space character between two words.

Input:
First line contains the number of test cases T. First line of every test case consists of N, denoting number of elements in array. Second line consists of elements in array. Third line consists of characters allowed per line.

Output:
Single line output,print 2*L spaced integers (where L is the number of lines required to adjust the words with given limit of character per line), denoting from which word to word in every line.(for more clearance of output, look the output in example).

Constraints:
1<=T<=100
1<=N<=100

Example:
Input:
2
4
3 2 2 5
6
3
3 2 2
4
Output:
1 1 2 3 4 4 
1 1 2 2 3 3 

For the first test case.
Line number 1: From word no. 1 to 1
Line number 2: From word no. 2 to 3
Line number 3: From word no. 4 to 4 

"""


def word_wrap():
    pass













inf=99999
t = 1#int(input())
for _ in range(t):
    n = 4#int(input())
    words = [3,2,2,5]#list(map(int, input().split()))
    l = 6#int(input())
    lc = [[inf for _ in range(n)] for _ in range(n)]
    sum, psum, minc, end = 0, 0, inf, n
    for i in range(n):
        sum += words[i]
        len = -1
        for j in range(i, n):
            len += words[j] + 1
            if len > l:
                break
            lc[i][j] = pow(l - len, 2)
    dp = [0] + [inf] * n
    p = [0] * (n+1)
    for i in range(n):
        psum += words[i]
        for j in range(i+1):
            if dp[i+1] > dp[j] + lc[j][i]:
                dp[i+1] = dp[j] + lc[j][i]
                p[i+1] = j
        if sum - psum + n - 1 - i < l and dp[i+1] < minc:
            minc = dp[i+1]
            end = i+1
    output = []
    if end < n:
        output += [n, end+1]
    while end != 0:
        # print(p[s]+1, s)
        output += [end, p[end]+1]
        end = p[end]
    print(' '.join(map(str, output[::-1])))
            











