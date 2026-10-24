class FreqStack:

    def __init__(self):
        self.freqs = defaultdict(int)
        self.stks = []

    def push(self, val: int) -> None:
        self.freqs[val] += 1
        if len(self.stks) < self.freqs[val]:
            self.stks.append([])
        self.stks[self.freqs[val] - 1].append(val)
        
    def pop(self) -> int:
        val = self.stks[-1].pop()
        if not self.stks[-1]:
            self.stks.pop()
        self.freqs[val] -= 1
        return val
        
        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()