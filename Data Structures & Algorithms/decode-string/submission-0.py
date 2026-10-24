class Solution:
    def decodeString(self, s: str) -> str:
        i = 0
        def recurse():
            nonlocal i
            ans = ""
            while i < len(s):
                if s[i] == ']':
                    i += 1
                    return ans
                elif '0' <= s[i] <= '9':
                    first_square = s.find('[', i+1)
                    prev = i
                    i = first_square + 1
                    ans += int(s[prev:first_square]) * recurse()
                else:
                    ans += s[i]
                    i += 1
            return ans
        return recurse()