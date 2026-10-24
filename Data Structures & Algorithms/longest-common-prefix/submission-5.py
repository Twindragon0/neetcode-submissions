class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        longestCommonPrefix = ""
        for i in range(len(strs[0])):
            for word in strs:
                if i >= len(word) or strs[0][i] != word[i]:
                    return longestCommonPrefix
            longestCommonPrefix += strs[0][i]
        return longestCommonPrefix

        
        