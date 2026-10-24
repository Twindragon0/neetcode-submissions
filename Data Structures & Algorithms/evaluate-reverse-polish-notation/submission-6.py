class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        def dfs():
            op = tokens.pop()
            if not(op == "+" or op == "-" or op == "*" or op == "/"):
                return int(op)
            
            right = dfs()
            left = dfs()
            if op == "+":
                return left + right
            if op == "-":
                return left - right
            if op == "*":
                return left * right
            if op == "/":
                return int(left / right)
        return dfs()
        