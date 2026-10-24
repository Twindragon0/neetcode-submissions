class MinStack:
    def __init__(self):
        self.stk = [] # val - oldMin
        self.currMin = 0

    def push(self, val: int) -> None:
        if not self.stk:
            self.stk.append(0)
            self.currMin = val
        elif val - self.currMin < 0:
            self.stk.append(val - self.currMin)
            self.currMin = val
        else:
            self.stk.append(val - self.currMin)

    def pop(self) -> None:
        # val - (val - oldMin) = oldMin
        if self.stk[-1] < 0:
            self.currMin = (self.currMin) - self.stk[-1]
        self.stk.pop()
        
    def top(self) -> int:
        # val - oldMin + oldMin
        if self.stk[-1] < 0:
            return self.currMin
        else:
            return self.stk[-1] + self.currMin

    def getMin(self) -> int:
        return self.currMin
        
        
