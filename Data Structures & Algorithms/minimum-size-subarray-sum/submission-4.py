class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        ans = 0
        for i in range(len(nums)):
            currSum = 0
            for j in range(i, len(nums)):
                currSum += nums[j]
                if currSum >= target:
                    ans = (j-i+1) if ans == 0 else min(ans, j-i+1)
                    break
        return ans

        