class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        r = 0
        currSum = 0
        minSize = 0
        while r < len(nums):
            currSum += nums[r]
            while currSum >= target:
                minSize = (r-l+1) if minSize == 0 else min(minSize, (r-l+1))
                currSum -= nums[l]
                l += 1
            r += 1
        return minSize
