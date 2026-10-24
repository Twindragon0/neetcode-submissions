class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stk = []
        for i, operation in enumerate(operations):
            if operation == "+":
                stk.append(stk[-1] + stk[-2])
            elif operation == "D":
                stk.append(stk[-1] * 2)
            elif operation == "C":
                stk.pop()
            else:
                stk.append(int(operation))
        return sum(stk)

