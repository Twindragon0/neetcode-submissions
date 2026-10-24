class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        memo = [[-1] * len(obstacleGrid[0]) for _ in range(len(obstacleGrid))]
        def recurse(i, j):
            if i >= len(obstacleGrid) or j >= len(obstacleGrid[0]) or obstacleGrid[i][j] == 1:
                return 0
            if i == len(obstacleGrid)-1 and j == len(obstacleGrid[0])-1:
                return 1
            if memo[i][j] != -1:
                return memo[i][j]
            memo[i][j] = recurse(i+1, j) + recurse(i, j+1)
            return memo[i][j]
        return recurse(0, 0)