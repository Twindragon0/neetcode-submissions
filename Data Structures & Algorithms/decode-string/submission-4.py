class Solution:
    def decodeString(self, s: str) -> str:
        stk = []
        for i in range(len(s)):
            if s[i] != ']':
                stk.append(s[i])
            else:
                substr = ""
                while stk[-1] != '[':
                    substr = stk.pop() + substr
                stk.pop()
                num = ""
                while stk and stk[-1].isdigit():
                    num = stk.pop() + num
                stk.append(int(num) * substr)
        return "".join(stk)