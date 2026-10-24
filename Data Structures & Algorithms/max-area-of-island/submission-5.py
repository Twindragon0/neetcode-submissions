class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxAns = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j]:
                    queue = deque()
                    ans = 0
                    grid[i][j] = 0
                    queue.append((i, j))
                    while queue:
                        row, col = queue.popleft()
                        ans += 1
                        if row+1 < len(grid) and grid[row+1][col]:
                            queue.append((row+1, col))
                            grid[row+1][col] = 0
                        if row-1 >= 0 and grid[row-1][col]:
                            queue.append((row-1, col))
                            grid[row-1][col] = 0
                        if col+1 < len(grid[row]) and grid[row][col+1]:
                            queue.append((row, col+1))
                            grid[row][col+1] = 0
                        if col-1 >= 0 and grid[row][col-1]:
                            queue.append((row, col-1))
                            grid[row][col-1] = 0
                    maxAns = max(maxAns, ans)
        return maxAns
