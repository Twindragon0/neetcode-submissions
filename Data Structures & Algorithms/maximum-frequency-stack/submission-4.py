class FreqStack:

    def __init__(self):
        self.freqs = defaultdict(int)
        self.heap = []
        self.i = 0

    def push(self, val: int) -> None:
        self.freqs[val] += 1
        heapq.heappush(self.heap, (-self.freqs[val], -self.i, val))
        self.i += 1
        
    def pop(self) -> int:
        _, _, val = heapq.heappop(self.heap)
        self.freqs[val] -= 1
        return val
        
        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()