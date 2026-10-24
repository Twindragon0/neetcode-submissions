class MinStack:
    def __init__(self):
        self.stk = []
        self.minEls = []

    def push(self, val: int) -> None:
        self.stk.append(val)
        if self.minEls:
            self.minEls.append(min(val, self.minEls[-1]))
        else:
            self.minEls.append(val)
        
    def pop(self) -> None:
        self.stk.pop()
        self.minEls.pop()
        
    def top(self) -> int:
        return self.stk[-1]

    def getMin(self) -> int:
        return self.minEls[-1]
        
        
