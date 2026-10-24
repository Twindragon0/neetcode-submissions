class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS = len(matrix)
        COLS = len(matrix[0])
        left = 0
        right = ROWS * COLS - 1
        while left <= right:
            mid = (left + right) // 2
            if matrix[mid // COLS][mid % COLS] < target:
                left = mid + 1
            elif matrix[mid // COLS][mid % COLS] > target:
                right = mid - 1
            else:
                return True
        return False