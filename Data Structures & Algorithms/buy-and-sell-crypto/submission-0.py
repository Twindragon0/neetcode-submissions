class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        minSoFar = prices[0]
        for i in range(1, len(prices)):
            if prices[i] > minSoFar:
                maxProfit = max(maxProfit, prices[i] - minSoFar)
            else:
                minSoFar = prices[i]
        return maxProfit