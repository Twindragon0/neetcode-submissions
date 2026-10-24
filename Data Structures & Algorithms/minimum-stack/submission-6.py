class MinStack:
    def __init__(self):
        self.stk = []
        self.minEl = []

    def push(self, val: int) -> None:
        if not self.stk:
            self.minEl.append(val)
        else:
            self.minEl.append(min(self.minEl[-1], val))
        self.stk.append(val)
        
    def pop(self) -> None:
        self.stk.pop()
        self.minEl.pop()
        
    def top(self) -> int:
        return self.stk[-1]

    def getMin(self) -> int:
        return self.minEl[-1]
        
        
