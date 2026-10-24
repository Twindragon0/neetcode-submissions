class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        longestPrefix = ""
        curr = 0
        while True:
            for currStr in strs:
                if curr >= len(currStr) or curr >= len(strs[0]) or currStr[curr] != strs[0][curr]:
                    return longestPrefix
            longestPrefix += strs[0][curr]
            curr += 1
        return longestPrefix

        