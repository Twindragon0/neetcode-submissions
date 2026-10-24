class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        minSoFar = nums[0] # min product including i
        maxSoFar = nums[0] # max product including i
        ans = nums[0]
        for i in range(1, len(nums)):
            tmp = maxSoFar * nums[i]
            maxSoFar = max(nums[i], minSoFar * nums[i], maxSoFar * nums[i])
            minSoFar = min(nums[i], minSoFar * nums[i], tmp)
            ans = max(ans, maxSoFar)
        return ans