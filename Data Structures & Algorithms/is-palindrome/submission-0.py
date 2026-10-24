class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1
        while left < right:
            if not('a' <= s[left] <= 'z' or 'A' <= s[left] <= 'Z' or '0' <= s[left] <= '9'):
                left += 1
            elif not('a' <= s[right] <= 'z' or 'A' <= s[right] <= 'Z' or '0' <= s[right] <= '9'):
                right -= 1
            elif s[left].lower() != s[right].lower():
                return False
            else:
                left += 1
                right -= 1
        return True
