class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = [0] * (target+1)
        for i in range(1, target+1):
            for num in nums:
                if i-num < 0:
                    continue
                dp[i] += dp[i-num] if i-num != 0 else 1
        return dp[-1]
