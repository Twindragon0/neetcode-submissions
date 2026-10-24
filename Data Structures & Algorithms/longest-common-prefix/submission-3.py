class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        strs = sorted(strs)
        longestCommonPrefix = ""
        for i in range(len(strs[0])):
            if i < len(strs[-1]) and strs[-1][i] == strs[0][i]:
                longestCommonPrefix += strs[0][i]
            else:
                return longestCommonPrefix
        return longestCommonPrefix
        
        