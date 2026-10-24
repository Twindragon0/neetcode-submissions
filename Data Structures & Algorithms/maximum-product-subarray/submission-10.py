class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        ans = float("-inf")
        prefix, suffix = 1, 1
        n = len(nums)
        for i in range(len(nums)):
            prefix = prefix*nums[i] if prefix != 0 else nums[i]
            suffix = suffix*nums[n-i-1] if suffix != 0 else nums[n-i-1]
            ans = max(ans, prefix, suffix)
        return ans