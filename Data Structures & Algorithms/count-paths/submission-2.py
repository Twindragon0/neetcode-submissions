class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = [[-1] * n for _ in range(m)]
        def recurse(i, j):
            if i >= m or j >= n:
                return 0
            if i == m-1 and j == n-1:
                return 1
            if memo[i][j] != -1:
                return memo[i][j]
            memo[i][j] = recurse(i+1, j) + recurse(i, j+1)
            return memo[i][j]
        return recurse(0,0)
        
