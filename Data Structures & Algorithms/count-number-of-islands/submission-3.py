class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        def dfs(i, j):
            if (i, j) in visited:
                return
            if i >= len(grid) or i < 0 or j >= len(grid[i]) or j < 0 or grid[i][j] == "0":
                return
            visited.add((i, j))
            grid[i][j] = "0"
            dfs(i+1, j)
            dfs(i, j+1)
            dfs(i-1, j)
            dfs(i, j-1)
        ans = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == "1":
                    dfs(i, j)
                    ans += 1
        return ans 
        
