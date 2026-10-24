class Solution:
    def isValid(self, s: str) -> bool:
        stk = []
        for char in s:
            if char in ['(', '[', '{']:
                stk.append(char)
            elif char == '}':
                if not(stk and stk.pop() == '{'):
                    return False
            elif char == ')':
                if not(stk and stk.pop() == '('):
                    return False
            elif char == ']':
                if not(stk and stk.pop() == '['):
                    return False
        return not stk
