class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = deque()
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 2:
                    queue.append((i, j, 0))
        
        ans = 0
        while queue:
            numEls = len(queue)
            for i in range(numEls):
                row, col, curr = queue.popleft()
                ans = max(ans, curr)
                if row+1 < len(grid) and grid[row+1][col] == 1:
                    queue.append((row+1, col, curr+1))
                    grid[row+1][col] = -1
                if row-1 >= 0 and grid[row-1][col] == 1:
                    queue.append((row-1, col, curr+1))
                    grid[row-1][col] = -1
                if col+1 < len(grid[row]) and grid[row][col+1] == 1:
                    queue.append((row, col+1, curr+1))
                    grid[row][col+1] = -1
                if col-1 >= 0 and grid[row][col-1] == 1:
                    queue.append((row, col-1, curr+1))
                    grid[row][col-1] = -1
        
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    return -1
        return ans