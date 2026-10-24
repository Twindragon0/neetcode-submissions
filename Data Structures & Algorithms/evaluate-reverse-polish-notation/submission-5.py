class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stk = []
        for token in tokens:
            if token == "+":
                first = stk.pop()
                second = stk.pop()
                stk.append(first + second)
            elif token == "-":
                first = stk.pop()
                second = stk.pop()
                stk.append(second - first)
            elif token == "*":
                first = stk.pop()
                second = stk.pop()
                stk.append(first * second)
            elif token == "/":
                first = stk.pop()
                second = stk.pop()
                stk.append(int(second / first))
            else:
                stk.append(int(token))
        return stk[-1]
        