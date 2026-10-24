class Solution:
    def decodeString(self, s: str) -> str:
        self.i = 0
        def recurse():
            ans = ""
            while self.i < len(s):
                if s[self.i] == ']':
                    self.i += 1
                    return ans
                elif '0' <= s[self.i] <= '9':
                    first_square = s.find('[', self.i+1)
                    num = int(s[self.i:first_square])
                    self.i = first_square + 1
                    ans += num * recurse()
                else:
                    ans += s[self.i]
                    self.i += 1
            return ans
        return recurse()