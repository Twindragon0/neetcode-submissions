class Solution:
    def decodeString(self, s: str) -> str:
        stringStk = []
        countStk = []
        curr = ""
        k = 0
        for c in s:
            if c == '[':
                stringStk.append(curr)
                countStk.append(k)
                k = 0
                curr = ""
            elif c == ']':
                curr = stringStk.pop() + curr * countStk.pop()
            elif c.isdigit():
                k = 10 * k + int(c)
            else:
                curr += c
        return curr