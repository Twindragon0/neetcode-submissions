class Solution:
    def validPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1
        while left < right:
            if s[left] == s[right]:
                left += 1
                right -= 1
            else:
                leftPlus = s[left+1:right+1]
                rightMinus = s[left:right]
                return leftPlus == leftPlus[::-1] or rightMinus == rightMinus[::-1]
        return True