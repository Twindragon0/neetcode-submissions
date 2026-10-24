class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        r = 0
        ans = 0
        currSum = 0
        while r < len(nums):
            currSum += nums[r]
            while currSum >= target:
                ans = (r-l+1) if ans == 0 else min(ans, r-l+1)
                currSum -= nums[l]
                l += 1
            r += 1
        return ans

        