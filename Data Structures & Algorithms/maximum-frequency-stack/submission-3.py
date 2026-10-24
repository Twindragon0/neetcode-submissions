class FreqStack:

    def __init__(self):
        self.freqs = defaultdict(int)
        self.stk = []

    def push(self, val: int) -> None:
        self.stk.append(val)
        self.freqs[val] += 1
        
    def pop(self) -> int:
        maxValue = max(self.freqs.values())
        i = len(self.stk) - 1
        while i >= 0 and self.freqs[self.stk[i]] != maxValue:
            i -= 1
        self.freqs[self.stk[i]] -= 1
        return self.stk.pop(i)
        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()