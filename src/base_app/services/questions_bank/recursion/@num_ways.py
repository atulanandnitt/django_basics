#https://www.youtube.com/watch?v=qli-JCrSwuk

def helper_dp(data, k, memo):
    if k ==0:
        return 1

    s= len(data) -k

    if data[s] == '0':
        return 0
    if memo[k] != None:
        return memo[k]
    result = helper_dp(data, k-1, memo)
    if k>=2 and int(data[s:s+2]) <=26:
        result += helper_dp(data, k-2, memo)
    memo[k] = result
    return result

def num_ways_dp(data):
    memo = new int[len(data) +1]
    return helper_dp(data, len(data), memo)

#print(num_ways_dp("12345"))


def helper(str1, k):
    if k == 0:
        return 1
    s = len(str1) - k
    if str1[s] == '0':
        return 0
    result = helper(str1, k-1)
    if k >= 2 and int(str1[s:s+2]) <= 26:
        result += helper(str1, k-2)

    return result



def num_ways(data):
    return helper(data, len(data))


print(num_ways("12345"))
