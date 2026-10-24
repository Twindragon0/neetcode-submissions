class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stk = []
        for token in tokens:
            if token == "+":
                stk.append(stk.pop() + stk.pop())
            elif token == "*":
                stk.append(stk.pop() * stk.pop())
            elif token == "-":
                second = stk.pop()
                first = stk.pop()
                stk.append(first - second)
            elif token == "/":
                second = stk.pop()
                first = stk.pop()
                stk.append(int(first / second))
            else:
                stk.append(int(token))
            print(stk)
        return stk[-1]
        