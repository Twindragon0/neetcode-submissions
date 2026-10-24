class StockSpanner:
    
    def __init__(self):
        self.res = []

    def next(self, price: int) -> int:
        if not self.res:
            self.res.append((price, 1))
            return 1
        else:
            ans = 1
            while self.res and self.res[-1][0] <= price:
                ans += self.res[-1][1]
                self.res.pop()
            self.res.append((price, ans))
            return ans
        
        
        
# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)