class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def recurseRow(l, r):
            if l > r:
                return -1
            mid = (l+r) // 2
            if mid == len(matrix)-1 or matrix[mid][0] <= target < matrix[mid+1][0]:
                return mid
            elif matrix[mid][0] > target:
                return recurseRow(l, mid-1)
            else:
                return recurseRow(mid+1, r)
        rowNum = recurseRow(0, len(matrix)-1)
        if rowNum == -1:
            return False
        left = 0
        right = len(matrix[rowNum])-1
        while left <= right:
            mid = (left+right) // 2
            if matrix[rowNum][mid] > target:
                right = mid-1
            elif matrix[rowNum][mid] < target:
                left = mid+1
            else:
                return True
        return False