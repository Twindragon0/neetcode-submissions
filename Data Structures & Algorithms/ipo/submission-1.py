class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        currK = 0
        capitalProfit = [] # min heap ordered by (capital, profit)
        profit = [] # max heap ordered by (profit)

        for i in range(len(profits)):
            capitalProfit.append((capital[i], profits[i]))
        capitalProfit.sort()
        i = 0
        while currK < k:
            while i < len(capitalProfit) and capitalProfit[i][0] <= w:
                heapq.heappush(profit, -capitalProfit[i][1])
                i += 1
            if not profit:
                break
            p = -heapq.heappop(profit)
            w += p
            currK += 1
        return w
        