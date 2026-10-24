class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        currK = 0
        capitalProfit = [] # min heap ordered by (capital, profit)
        profit = [] # max heap ordered by (profit)

        for i in range(len(profits)):
            heapq.heappush(capitalProfit, (capital[i], profits[i]))
        while currK < k:
            while capitalProfit and capitalProfit[0][0] <= w:
                heapq.heappush(profit, -heapq.heappop(capitalProfit)[1])
            if not profit:
                break
            p = -heapq.heappop(profit)
            w += p
            currK += 1
        return w
        