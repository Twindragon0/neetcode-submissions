class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        numOnes = 0
        numEdges = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j]:
                    numOnes += 1
                    if i+1 < len(grid) and grid[i+1][j]:
                        numEdges += 1
                    if i-1 >= 0 and grid[i-1][j]:
                        numEdges += 1
                    if j+1 < len(grid[i]) and grid[i][j+1]:
                        numEdges += 1
                    if j-1 >= 0 and grid[i][j-1]:
                        numEdges += 1
        return 4 * numOnes - numEdges