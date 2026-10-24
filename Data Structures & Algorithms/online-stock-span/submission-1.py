class StockSpanner:
    
    def __init__(self):
        self.prices = []
        self.res = []

    def next(self, price: int) -> int:
        if not self.res:
            self.res.append(1)
            self.prices.append(price)
            return 1
        else:
            j = len(self.prices) - 1
            ans = 1
            while j >= 0 and self.prices[j] <= price:
                ans += self.res[j]
                j -= self.res[j]
            self.res.append(ans)
            self.prices.append(price)
            return ans
        
        
        
# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)