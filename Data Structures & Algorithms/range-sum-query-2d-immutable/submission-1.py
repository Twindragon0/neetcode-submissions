class NumMatrix:
    def __init__(self, matrix: List[List[int]]):
        self.prefixSums = matrix
        for i in range(len(matrix) - 1, -1, -1):
            for j in range(len(matrix[i]) - 1, -1, -1):
                self.prefixSums[i][j] = matrix[i][j]
                if j+1 < len(matrix[i]):
                    self.prefixSums[i][j] += matrix[i][j+1]
                if i+1 < len(matrix):
                    self.prefixSums[i][j] += matrix[i+1][j]
                if i+1 < len(matrix) and j+1 < len(matrix[i]):
                    self.prefixSums[i][j] -= matrix[i+1][j+1]
        print(self.prefixSums)
        
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        ans = self.prefixSums[row1][col1]
        if row2+1 < len(self.prefixSums):
            ans -= self.prefixSums[row2+1][col1]
        if col2+1 < len(self.prefixSums[0]):
            ans -= self.prefixSums[row1][col2+1]
        if row2+1 < len(self.prefixSums) and col2+1 < len(self.prefixSums[0]):
            ans += self.prefixSums[row2+1][col2+1]
        return ans
        
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)