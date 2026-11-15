class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        res = [[(False, False) for _ in range(len(heights[0]))] for _ in range(len(heights))]
        # Initial atlantic + pacific
        pacificQueue = deque()
        pacificVisited = set()
        atlanticQueue = deque()
        atlanticVisited = set()
        for i in range(len(res)):
            res[i][0] = (True, res[i][0][1])
            if (i, 0) not in pacificVisited:
                pacificVisited.add((i, 0))
                pacificQueue.append((i, 0))
            res[i][-1] = (res[i][-1][0], True)
            if (i, len(res[0])-1) not in atlanticVisited:
                atlanticVisited.add((i, len(res[0])-1))
                atlanticQueue.append((i, len(res[0])-1))
        for j in range(len(res[0])):
            res[0][j] = (True, res[0][j][1])
            if (0, j) not in pacificVisited:
                pacificVisited.add((0, j))
                pacificQueue.append((0, j))
            res[-1][j] = (res[-1][j][0], True)
            if (len(res)-1, j) not in atlanticVisited:
                atlanticVisited.add((len(res)-1, j))
                atlanticQueue.append((len(res)-1, j))
        while atlanticQueue:
            row, col = atlanticQueue.popleft()
            if row+1 < len(res) and (row+1, col) not in atlanticVisited and heights[row+1][col] >= heights[row][col]:
                res[row+1][col] = (res[row+1][col][0], True)
                atlanticVisited.add((row+1, col))
                atlanticQueue.append((row+1, col))
            if row-1 >= 0 and (row-1, col) not in atlanticVisited and heights[row-1][col] >= heights[row][col]:
                res[row-1][col] = (res[row-1][col][0], True)
                atlanticVisited.add((row-1, col))
                atlanticQueue.append((row-1, col))
            if col+1 < len(res[0]) and (row, col+1) not in atlanticVisited and heights[row][col+1] >= heights[row][col]:
                res[row][col+1] = (res[row][col+1][0], True)
                atlanticVisited.add((row, col+1))
                atlanticQueue.append((row, col+1))
            if col-1 >= 0 and (row, col-1) not in atlanticVisited and heights[row][col-1] >= heights[row][col]:
                res[row][col-1] = (res[row][col-1][0], True)
                atlanticVisited.add((row, col-1))
                atlanticQueue.append((row, col-1))
        while pacificQueue:
            row, col = pacificQueue.popleft()
            if row+1 < len(res) and (row+1, col) not in pacificVisited and heights[row+1][col] >= heights[row][col]:
                res[row+1][col] = (True, res[row+1][col][1])
                pacificVisited.add((row+1, col))
                pacificQueue.append((row+1, col))
            if row-1 >= 0 and (row-1, col) not in pacificVisited and heights[row-1][col] >= heights[row][col]:
                res[row-1][col] = (True, res[row-1][col][1])
                pacificVisited.add((row-1, col))
                pacificQueue.append((row-1, col))
            if col+1 < len(res[0]) and (row, col+1) not in pacificVisited and heights[row][col+1] >= heights[row][col]:
                res[row][col+1] = (True, res[row][col+1][1])
                pacificVisited.add((row, col+1))
                pacificQueue.append((row, col+1))
            if col-1 >= 0 and (row, col-1) not in pacificVisited and heights[row][col-1] >= heights[row][col]:
                res[row][col-1] = (True, res[row][col-1][1])
                pacificVisited.add((row, col-1))
                pacificQueue.append((row, col-1))
        ans = []
        for i in range(len(res)):
            for j in range(len(res[i])):
                if res[i][j] == (True, True):
                    ans.append([i, j])
        return ans
        
        
        