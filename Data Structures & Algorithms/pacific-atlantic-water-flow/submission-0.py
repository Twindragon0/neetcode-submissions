class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        dp = [[[False, False] for _ in range(len(heights[0]))] for _ in range(len(heights))]
        queue = deque()
        ans = []
        def initialPopulate(isAtlantic):
            for j in range(len(heights[0])):
                row = -1 if isAtlantic else 0
                dp[row][j][isAtlantic] = True
                if dp[row][j][not isAtlantic]:
                    ans.append((row % len(heights), j % len(heights[0])))
                queue.append((row % len(heights), j % len(heights[0])))
            for i in range(1-isAtlantic, len(heights)-isAtlantic):
                col = -1 if isAtlantic else 0
                dp[i][col][isAtlantic] = True
                if dp[i][col][not isAtlantic]:
                    ans.append((i % len(heights), col % len(heights[0])))
                queue.append((i % len(heights), col % len(heights[0])))
        def bfs(isAtlantic):
            while queue:
                row, col = queue.popleft()
                if row+1 < len(heights) and heights[row+1][col] >= heights[row][col] and not dp[row+1][col][isAtlantic]:
                    queue.append((row+1, col))
                    dp[row+1][col][isAtlantic] = True
                    if dp[row+1][col][not isAtlantic]:
                        ans.append((row+1, col))
                if row-1 >= 0 and heights[row-1][col] >= heights[row][col] and not dp[row-1][col][isAtlantic]:
                    queue.append((row-1, col))
                    dp[row-1][col][isAtlantic] = True
                    if dp[row-1][col][not isAtlantic]:
                        ans.append((row-1, col))
                if col+1 < len(heights[0]) and heights[row][col+1] >= heights[row][col] and not dp[row][col+1][isAtlantic]:
                    queue.append((row, col+1))
                    dp[row][col+1][isAtlantic] = True
                    if dp[row][col+1][not isAtlantic]:
                        ans.append((row, col+1))
                if col-1 >= 0 and heights[row][col-1] >= heights[row][col] and not dp[row][col-1][isAtlantic]:
                    queue.append((row, col-1))
                    dp[row][col-1][isAtlantic] = True
                    if dp[row][col-1][not isAtlantic]:
                        ans.append((row, col-1))
        # populating da pacific
        initialPopulate(False)
        bfs(False)
        # populating da atlantic
        initialPopulate(True)
        bfs(True)
        return ans

        