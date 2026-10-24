class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def recurse(i, j):
            if not (0 <= i < len(grid) and 0 <= j < len(grid[0])):
                return 0
            if grid[i][j] == 0:
                return 0
            grid[i][j] = 0
            return 1 + recurse(i+1, j) + recurse(i, j+1) + recurse(i-1, j) + recurse(i, j-1)
        ans = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]:
                    ans = max(ans, recurse(i, j))
        return ans
