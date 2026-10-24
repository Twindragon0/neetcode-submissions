class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        ans = nums[0]
        prefixSum = nums[0]
        maxNeg = nums[0] if nums[0] < 0 else float("-inf")
        minPos = nums[0] if nums[0] > 0 else float("inf")
        for i in range(1, len(nums)):
            if prefixSum == 0:
                prefixSum = nums[i]
            else:
                prefixSum *= nums[i]
            ans = max(ans, prefixSum, prefixSum // maxNeg if maxNeg != 0 else prefixSum, prefixSum // minPos if minPos != 0 else prefixSum)
            if prefixSum > 0:
                minPos = min(minPos, prefixSum)
            elif prefixSum < 0:
                maxNeg = max(maxNeg, prefixSum)
        return ans