class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        low = 1
        high = len(nums)
        while low < high:
            mid = (low + high) // 2
            count = 0
            for num in nums:
                count = count+1 if num <= mid else count
            if count <= mid:
                low = mid + 1
            else:
                high = mid
        return high
            