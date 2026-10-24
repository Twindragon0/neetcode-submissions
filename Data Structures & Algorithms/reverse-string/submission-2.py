class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        stk = []
        for char in s:
            stk.append(char)
        i = 0
        while stk:
            s[i] = stk.pop()
            i += 1