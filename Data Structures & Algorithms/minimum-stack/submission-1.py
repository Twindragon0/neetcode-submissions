class MinStack:
    def __init__(self):
        self.currTop = -1
        self.stk = []
        self.minEls = []

    def push(self, val: int) -> None:
        self.currTop += 1
        if self.currTop == len(self.stk):
            self.stk.append(val)
            self.minEls.append(val if self.currTop == 0 else min(self.minEls[self.currTop-1], val))
        else:
            self.stk[self.currTop] = val
            self.minEls[self.currTop] = val if self.currTop == 0 else min(self.minEls[self.currTop-1], val)

    def pop(self) -> None:
        self.currTop -= 1

    def top(self) -> int:
        return self.stk[self.currTop]

    def getMin(self) -> int:
        return self.minEls[self.currTop]
