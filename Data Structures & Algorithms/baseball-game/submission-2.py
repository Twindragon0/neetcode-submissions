class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stk = []
        ans = 0
        for i, operation in enumerate(operations):
            if operation == "+":
                ans += stk[-1] + stk[-2]
                stk.append(stk[-1] + stk[-2])
            elif operation == "D":
                ans += stk[-1] * 2
                stk.append(stk[-1] * 2)
            elif operation == "C":
                ans -= stk.pop()
            else:
                stk.append(int(operation))
                ans += int(operation)
        return ans

