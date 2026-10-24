class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        curr = 0
        ans = ""
        while curr < min(len(word1), len(word2)):
            ans += word1[curr]
            ans += word2[curr]
            curr += 1
        if curr < len(word1):
            ans += word1[curr:]
        else:
            ans += word2[curr:]
        return ans