class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left = 0
        right = len(matrix) - 1
        rowIdx = -1
        while left <= right:
            mid = (left + right) // 2
            if mid == len(matrix) - 1 or matrix[mid][0] <= target < matrix[mid+1][0]:
                rowIdx = mid
                break
            elif matrix[mid][0] < target:
                left = mid + 1
            else:
                right = mid - 1
        if rowIdx == -1:
            return False
        left = 0
        right = len(matrix[rowIdx]) - 1
        while left <= right:
            mid = (left + right) // 2
            if matrix[rowIdx][mid] > target:
                right = mid - 1
            elif matrix[rowIdx][mid] < target:
                left = mid + 1
            else:
                return True
        return False