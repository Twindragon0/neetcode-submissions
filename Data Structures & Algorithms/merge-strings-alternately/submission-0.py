class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        left = 0
        right = 0
        ans = ""
        while left < len(word1) or right < len(word2):
            if left < len(word1):
                ans += word1[left]
                left += 1
            if right < len(word2):
                ans += word2[right]
                right += 1
        return ans