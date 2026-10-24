class MyStack:

    def __init__(self):
        self.q1 = None

    def push(self, x: int) -> None:
        # x, y
        # [y, [x, []]]
        self.q1 = deque([x, self.q1])
    
    def pop(self) -> int:
        val = self.q1.popleft()
        self.q1 = self.q1.popleft()
        return val
        
    def top(self) -> int:
        return self.q1[0]

    def empty(self) -> bool:
        return not self.q1
        

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()