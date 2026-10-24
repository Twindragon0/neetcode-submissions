class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        numOnes = 0
        numEdges = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    numOnes += 1
                    if j+1 < len(grid[i]):
                        numEdges += grid[i][j+1]
                    if i+1 < len(grid):
                        numEdges += grid[i+1][j]
                    if j-1 >= 0:
                        numEdges += grid[i][j-1]
                    if i-1 >= 0:
                        numEdges += grid[i-1][j]
        return 4 * numOnes - numEdges