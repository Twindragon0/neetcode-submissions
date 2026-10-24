class Solution:
    def isPalindrome(self, s: str) -> bool:
        # c.isalnum()
        newStr = ""
        for c in s:
            if c.isalnum():
                newStr += c.lower()
        return newStr == newStr[::-1]
