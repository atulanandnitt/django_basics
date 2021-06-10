class Solution:
    # def findJudge(self, N: int, trust: List[List[int]]) -> int:
    def findJudge(self, N: int, trust) -> int:
        if not len(trust) and N < 2: return 1
        count = [0] * (N+1)
        # count = [0 for i in range(N+1)]
        # print("N : ", N)
        # count = list()
        # for i in range(N+1):
        #     count.append(0)
        for i, j in trust:
            print(i, j)
            count[i] -= 1
            count[j] += 1
        v = max(count)
        return count.index(v) if v == N - 1 else -1

N = 4
trust = [[1,3],[1,4],[2,3],[2,4],[4,3]]

s1 = Solution()
print(s1.findJudge(N, trust))
