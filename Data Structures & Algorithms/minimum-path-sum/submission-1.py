class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        memo = [[-1] * len(grid[0]) for _ in range(len(grid))]
        def recurse(i, j):
            if i >= len(grid) or j >= len(grid[0]):
                return float("inf")
            if i == len(grid)-1 and j == len(grid[0])-1:
                return grid[i][j]
            if memo[i][j] != -1:
                return memo[i][j]
            memo[i][j] = grid[i][j] + min(recurse(i+1, j), recurse(i, j+1))
            return memo[i][j]
        return recurse(0, 0)
