# https://leetcode.com/explore/challenge/card/may-leetcoding-challenge/537/week-4-may-22nd-may-28th/3337/

class Solution:
    def frequencySort(self, s: str) -> str:
        dict1 = {key: s.count(key) for key in set(s)}
        sol = sorted(dict1, key=lambda x:dict1[x], reverse=True)
        result = ''
        for char in sol:
            result += char * dict1[char]
        return result