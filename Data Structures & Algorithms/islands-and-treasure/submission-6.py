class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        queue = deque()
        visited = set()
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 0:
                    queue.append((i, j, 0))
                    visited.add((i, j))
        while queue:
            numTimes = len(queue)
            for i in range(numTimes):
                row, col, curr = queue.popleft()
                if row+1 < len(grid) and (row+1, col) not in visited and grid[row+1][col] != -1:
                    grid[row+1][col] = curr+1
                    visited.add((row+1, col))
                    queue.append((row+1, col, curr+1))
                if row-1 >= 0 and (row-1, col) not in visited and grid[row-1][col] != -1:
                    grid[row-1][col] = curr+1
                    visited.add((row-1, col))
                    queue.append((row-1, col, curr+1))
                if col+1 < len(grid[row]) and (row, col+1) not in visited and grid[row][col+1] != -1:
                    grid[row][col+1] = curr+1
                    visited.add((row, col+1))
                    queue.append((row, col+1, curr+1))
                if col-1 >= 0 and (row, col-1) not in visited and grid[row][col-1] != -1:
                    grid[row][col-1] = curr+1
                    visited.add((row, col-1))
                    queue.append((row, col-1, curr+1))
                

