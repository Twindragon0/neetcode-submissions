class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans, prefixSum, least = nums[0], nums[0], nums[0]
        for i in range(1, len(nums)):
            prefixSum += nums[i]
            ans = max(ans, prefixSum, prefixSum-least)
            least = min(least, prefixSum)
        return ans