class Solution:
    # def countSquares(self, matrix: List[List[int]]) -> int:
    def countSquares(self, matrix) -> int:
        m,n = len(matrix),  len(matrix[0])
        print(matrix)
        print(m, n)
        sol = 0
        dp = [[0 for i in range(n+1)] for j in range(m+1)]
        for i in range(m+1):
            for j in range(n+1):
                if i==0 or j==0:
                    dp[i][j] = 0
                    continue
                if matrix[i-1][j-1] == 1:
                    dp[i][j] = 1 + min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1])
                sol += dp[i][j]

        return sol

s1 = Solution()
mat = [
  [1,0,1],
  [1,1,0],
  [1,1,0]
]
matrix = [
  [0,1,1,1],
  [1,1,1,1],
  [0,1,1,1]
]
print(s1.countSquares(mat))