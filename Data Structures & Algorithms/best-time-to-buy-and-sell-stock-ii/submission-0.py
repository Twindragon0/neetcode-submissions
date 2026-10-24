class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = defaultdict(int)
        def rec(i, isHolding):
            if i == len(prices):
                return 0
            if (i, isHolding) in dp:
                return dp[(i, isHolding)]
            ans = rec(i+1, isHolding)
            if isHolding:
                ans = max(ans, prices[i] + rec(i+1, False))
            else:
                ans = max(ans, -prices[i] + rec(i+1, True))
            dp[(i, isHolding)] = ans
            return ans
        return rec(0, False)
        