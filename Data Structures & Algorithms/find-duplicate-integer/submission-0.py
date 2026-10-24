class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for num in nums:
            val = abs(num)
            if nums[val-1] < 0:
                return val
            nums[val - 1] *= -1
        