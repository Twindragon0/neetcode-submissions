class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def dfs(i, j):
            if i >= len(grid) or i < 0 or j >= len(grid[i]) or j < 0 or grid[i][j] == 0:
                return 0
            grid[i][j] = 0
            return 1 + dfs(i+1, j) + dfs(i, j+1) + dfs(i-1, j) + dfs(i, j-1)
        ans = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j]:
                    ans = max(ans, dfs(i, j))
        return ans