class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        n = len(nums)
        dp = [[-1] * (k+1) for _ in range(n)] 
        def recurse(i, remaining):
            if i == n and remaining == 0:
                return 0
            if remaining == 0:
                return float("inf")
            if dp[i][remaining] != -1:
                return dp[i][remaining]
            res = float("inf")
            for endBucket in range(i, n-remaining+1):
                currSum = sum(nums[i:endBucket+1])
                res = min(res, max(currSum, recurse(endBucket+1, remaining-1)))
            dp[i][remaining] = res
            return res
        return recurse(0, k)
