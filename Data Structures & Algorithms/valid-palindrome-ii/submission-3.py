class Solution:
    def validPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1
        while left < right:
            if s[left] == s[right]:
                left += 1
                right -= 1
            else:
                leftStr = s[left+1:right+1]
                rightStr = s[left:right]
                return leftStr == leftStr[::-1] or rightStr == rightStr[::-1]
        return True