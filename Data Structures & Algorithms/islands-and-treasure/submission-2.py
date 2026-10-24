class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 0:
                    queue = deque()
                    queue.append((i+1, j, 1))
                    queue.append((i, j+1, 1))
                    queue.append((i-1, j, 1))
                    queue.append((i, j-1, 1))
                    while queue:
                        row, col, curr = queue.popleft()
                        if row >= len(grid) or row < 0 or col >= len(grid[0]) or col < 0:
                            continue
                        if grid[row][col] == -1 or grid[row][col] <= curr:
                            continue
                        grid[row][col] = curr
                        queue.append((row+1, col, curr+1))
                        queue.append((row, col+1, curr+1))
                        queue.append((row-1, col, curr+1))
                        queue.append((row, col-1, curr+1))
