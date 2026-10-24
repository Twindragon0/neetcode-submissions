class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        visited = set()
        def dfs(i, j):
            if (i, j) in visited:
                return 0
            if i >= len(grid) or i < 0 or j >= len(grid[i]) or j < 0 or grid[i][j] == 0:
                return 1
            visited.add((i, j))
            perimeter = dfs(i+1, j) + dfs(i, j+1) + dfs(i-1, j) + dfs(i, j-1)
            return perimeter
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j]:
                    return dfs(i, j)
