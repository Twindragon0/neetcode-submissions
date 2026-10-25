class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        heap = []
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                heapq.heappush(heap, (-matrix[i][j], (i, j)))
        self.memo = defaultdict(int)
        ans = 1
        while heap:
            curr = 1
            _, (row, col) = heapq.heappop(heap)
            if row+1 < len(matrix) and matrix[row+1][col] > matrix[row][col]:
                curr = max(curr, 1 + self.memo[(row+1, col)])
            if col+1 < len(matrix[0]) and matrix[row][col+1] > matrix[row][col]:
                curr = max(curr, 1 + self.memo[(row, col+1)])
            if row-1 >= 0 and matrix[row-1][col] > matrix[row][col]:
                curr = max(curr, 1 + self.memo[(row-1, col)])
            if col-1 >= 0 and matrix[row][col-1] > matrix[row][col]:
                curr = max(curr, 1 + self.memo[(row, col-1)])
            self.memo[(row, col)] = curr
            ans = max(ans, curr)   
        return ans