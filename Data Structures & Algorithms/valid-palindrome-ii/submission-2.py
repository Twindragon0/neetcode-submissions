class Solution:
    def validPalindrome(self, s: str) -> bool:
        isPalindrome = s == s[::-1]
        for i in range(len(s)):
            newStr = s[:i] + s[i+1:]
            isPalindrome = isPalindrome or newStr == newStr[::-1]
        return isPalindrome