class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        self.memo = defaultdict(int)
        def recurse(i, curr, isBought):
            if (i, curr, isBought) in self.memo:
                return self.memo[(i, curr, isBought)]
            if i >= len(prices):
                return curr
            maxVal = float("-inf")
            if not isBought:
                maxVal = max(maxVal, recurse(i+1, curr - prices[i], True))
            if isBought:
                maxVal = max(maxVal, recurse(i+2, curr + prices[i], False))
            maxVal = max(maxVal, recurse(i+1, curr, isBought))
            self.memo[(i, curr, isBought)] = maxVal
            return maxVal
        return recurse(0, 0, False)