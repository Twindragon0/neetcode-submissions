class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        seen = defaultdict(int)
        queue = deque()
        queue.append((0, 0))
        seen[(0, 0)] = 0
        while queue:
            row, col = queue.popleft()
            # check right
            if col+1 < len(heights[0]) and ((row, col+1) not in seen or seen[(row, col+1)] > max(seen[(row, col)], abs(heights[row][col] - heights[row][col+1]))):
                queue.append((row, col+1))
                seen[(row, col+1)] = max(seen[(row, col)], abs(heights[row][col] - heights[row][col+1]))
            if col-1 >= 0 and ((row, col-1) not in seen or seen[(row, col-1)] > max(seen[(row, col)], abs(heights[row][col] - heights[row][col-1]))):
                queue.append((row, col-1))
                seen[(row, col-1)] = max(seen[(row, col)], abs(heights[row][col] - heights[row][col-1]))
            if row+1 < len(heights) and ((row+1, col) not in seen or seen[(row+1, col)] > max(seen[(row, col)], abs(heights[row][col] - heights[row+1][col]))):
                queue.append((row+1, col))
                seen[(row+1, col)] = max(seen[(row, col)], abs(heights[row][col] - heights[row+1][col]))
            if row-1 >= 0 and ((row-1, col) not in seen or seen[(row-1, col)] > max(seen[(row, col)], abs(heights[row][col] - heights[row-1][col]))):
                queue.append((row-1, col))
                seen[(row-1, col)] = max(seen[(row, col)], abs(heights[row][col] - heights[row-1][col]))
        return seen[(len(heights)-1, len(heights[0])-1)]