class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        minPrefix = 0
        prefixSum = 0
        ans = float("-inf")
        for num in nums:
            prefixSum += num
            ans = max(ans, prefixSum-minPrefix)
            minPrefix = min(minPrefix, prefixSum)
        return ans