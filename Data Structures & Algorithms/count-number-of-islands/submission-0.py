class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def recurse(i, j):
            if not (0 <= i < len(grid) and 0 <= j < len(grid[0])):
                return
            if grid[i][j] == "0":
                return
            grid[i][j] = "0"
            recurse(i+1, j)
            recurse(i, j+1)
            recurse(i-1, j)
            recurse(i, j-1)
        
        ans = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == "1":
                    recurse(i, j)
                    ans += 1
        return ans

